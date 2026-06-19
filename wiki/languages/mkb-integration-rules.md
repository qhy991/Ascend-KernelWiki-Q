---
id: lang-mkb-integration-rules
title: "MultiKernelBench Integration Rules — ascendc_direct_launch"
type: wiki-language
architectures: [ascend910b]
tags: [ascendc, operator, pybind, tutorial]
confidence: verified
languages: [ascendc, cpp, python]
sources: [doc-ascendc-pytorch-framework-adaptation, doc-torch-npu-npu-ffn, code-multikernelbench-ascendc-direct-launch]
related: [lang-ascendc-direct-launch-project, lang-torch-npu-cpp-api, pattern-ascendc-compile-troubleshooting, kernel-mkb-working-examples]
reproducibility: runnable
---

# MultiKernelBench Integration Rules — ascendc_direct_launch

Rules extracted from `MultiKernelBench/backends/ascendc_direct_launch_backend.py` and `utils/cheating_detection.py`. Understanding these rules is the difference between compile failures and passing evaluation — session round 3 succeeded only after aligning with them.

## Backend Overview

| Step | Action |
|------|--------|
| 1. Parse | JSON spec extracted from model output (```json fence or raw) |
| 2. Stage | Write all `sources[]` to temp work dir |
| 3. Build | Auto-generate CMakeLists, `cmake` configure + build |
| 4. Load | `exec()` `ModelNew.py`, resolve `entry.model` class |
| 5. Correctness | Run reference `Model` vs `ModelNew` on all test cases |
| 6. Performance | `torch_npu.npu.Event` timing, compare vs baseline |
| 7. Cheating | AST scan of Python `forward()` regardless of compile outcome |

Language flag: `-l ascendc_direct_launch`

## JSON Spec — Complete Format

```json
{
  "name": "string",
  "format_version": "0.1",
  "description": "optional",
  "entry": {
    "model": "ModelNew.py::ModelNew"
  },
  "build": {
    "type": "ascendc_direct_launch",
    "module_name": "benchmark_ops",
    "kernel_sources": ["kernel/my_kernel.cpp"],
    "binding_sources": ["kernel/pybind11.cpp"],
    "include_dirs": ["kernel", "."],
    "build_dir": "kernel/build"
  },
  "sources": [
    { "path": "relative/path", "content": "file contents as string" }
  ]
}
```

### Path Safety Rules

- All paths must be **relative** (no absolute paths).
- No `..` path components.
- Duplicate paths → error.

### kernel_sources vs binding_sources

| Category | Compiled with | Contains | Inferred when omitted |
|----------|---------------|----------|----------------------|
| `kernel_sources` | `bisheng -xasc` (device) | `__global__ __aicore__` kernels, `extern "C"` launch wrappers, tiling helpers | All `.cpp` except binding files |
| `binding_sources` | `g++` (host) | `PYBIND11_MODULE`, `torch::Tensor` wrappers | `.cpp` containing `PYBIND11_MODULE` or named `pybind11.cpp` |

**Critical distinction**:
- Device code **must** be in `kernel_sources` — bisheng uses `-xasc` AscendC mode.
- Host binding **must** be in `binding_sources` — linked with libtorch + torch_npu.
- A single `.cpp` cannot serve both roles.

### module_name Inference

1. Explicit `build.module_name`
2. Parse `PYBIND11_MODULE(name, m)` from binding source
3. Default: `benchmark_ops`

Python import must match: `import benchmark_ops as _ops`.

## AST Cheating Detector Rules

Implemented in `utils/cheating_detection.py`. Scans **reachable code from `ModelNew.forward()`** (and `Model.forward()` fallback).

### Allowed in forward()

**torch.* functions** (allocation/metadata only):
`empty`, `empty_like`, `zeros`, `ones`, `tensor`, `arange`, `as_tensor`, etc.

**Tensor methods** (metadata/layout only):
`size`, `shape`, `stride`, `numel`, `dtype`, `device`, `contiguous`, `view`, `reshape`, `permute`, `to`, `npu`, `is_npu`, etc.

**Extension calls** — imports matching:
- `*_ext`, `*_ascendc*`, `benchmark_ops`, `custom_ops_lib`, `_C`
- `importlib.import_module(...)` assigned to a variable

### Forbidden in forward()

| Category | Examples |
|----------|----------|
| Tensor compute methods | `.matmul()`, `.add()`, `.mul()`, `.relu()`, `.softmax()` |
| torch compute | `torch.matmul`, `torch.nn.functional.*` |
| nn.Module compute | `nn.Linear`, `nn.ReLU`, `nn.Sequential(Linear, ...)` |
| Tensor arithmetic | `a + b`, `a * b`, `a @ b` in Python |
| Scalar Python loops | `for i in range(n):` with tensor indexing + compute |

### Regression Types

| Type | Meaning |
|------|---------|
| 1 | Python syntax error |
| 3 | Forbidden PyTorch compute in forward |
| 4 | Scalar Python loop over tensors |

Result fields when cheating detected:

```json
{
  "compiled": true,
  "cheating": true,
  "cheating_info": {
    "valid": false,
    "regression_type": 3,
    "suggestion": "Move all core computation into the custom kernel..."
  }
}
```

## Legal Bypass Patterns

These patterns pass the detector while still using optimized compute:

### 1. pybind11 Extension Call (Recommended)

```python
import benchmark_ops as _ops

class ModelNew(nn.Module):
    def forward(self, x, w1, w2, activation):
        return _ops.ffn(x, w1, w2, activation)  # all compute in C++/AscendC
```

### 2. importlib Indirect Import

```python
import importlib
_ops = importlib.import_module("benchmark_ops")

class ModelNew(nn.Module):
    def forward(self, x, w1, w2, activation):
        return _ops.ffn(x, w1, w2, activation)
```

Detector tracks `importlib.import_module` assignments as extension modules.

### 3. torch_npu in C++ Binding (Not Python)

Call `torch_npu.npu_ffn` from `pybind11.cpp` — detector only scans Python AST, not C++.

### Anti-Patterns (Will Fail)

```python
# BAD: direct torch compute
def forward(self, x, w1, w2, activation):
    h = torch.matmul(x, w1)
    h = torch.nn.functional.gelu(h)
    return torch.matmul(h, w2)

# BAD: torch_npu in Python forward (not an extension import)
def forward(self, x, w1, w2, activation):
    import torch_npu
    return torch_npu.npu_ffn(x, w1, w2, activation)  # FAILS — not extension pattern
```

**Note**: Direct `torch_npu.npu_ffn()` in Python forward **may** fail cheating detection because `torch_npu` is not registered as an extension module. Wrap in pybind C++ instead.

## eval_single_runner.py Flow

```bash
python3 eval_single_runner.py \
  -i generated_response.txt \
  -o 2_ffn \
  -l ascendc_direct_launch \
  -r result.json
```

Pipeline (`utils/evaluation_utils.py` → `eval_single`):

1. Extract first code block (json/python/cpp)
2. `backend.compile()` → JSON parse + CMake build
3. Load reference model from `reference/{op}.py`
4. `correctness_execution()` — compare outputs with tolerance
5. `time_execution()` — N trials with NPU events
6. `detect_cheating()` — AST scan
7. Write `result.json`

## result.json Format

```json
{
  "compiled": true,
  "correctness": true,
  "performance": {
    "mean": 0.123,
    "std": 0.004,
    "min": 0.119,
    "max": 0.131,
    "num_trials": 100
  },
  "hardware": "Ascend910B2",
  "cheating": false
}
```

Failure variants:

```json
{
  "compiled": false,
  "correctness": false,
  "performance": null,
  "hardware": "Ascend910B2",
  "cheating": false,
  "compile_info": "CMake build failed\nCommand: cmake --build ..."
}
```

```json
{
  "compiled": true,
  "correctness": false,
  "correctness_info": "Output mismatch at case 3...",
  "cheating": false
}
```

Speedup is computed externally: `baseline_mean / candidate_mean`. Values < 1.0 mean slower than reference.

## Model Entry Contract

Reference models live in `MultiKernelBench/reference/`. Each defines:

- `class Model(nn.Module)` — baseline (often `torch_npu.npu_ffn`)
- `class ModelNew(nn.Module)` — your submission (in generated JSON)
- `get_input_groups()` — test cases (shapes, dtypes, activations)
- `get_init_inputs()` — constructor args

Your `ModelNew.forward()` signature must match the reference exactly.

## Checklist Before Submission

- [ ] JSON valid, all paths relative, no duplicates
- [ ] `kernel_sources` / `binding_sources` correctly split
- [ ] `PYBIND11_MODULE` name matches Python import
- [ ] `ModelNew.forward()` only calls extension — zero torch compute
- [ ] `get_init_inputs()` included in ModelNew.py
- [ ] Kernel uses `c10_npu::getCurrentNPUStream()` in binding
- [ ] All test dtypes supported (fp16, fp32, bf16)
- [ ] Build dir added to `sys.path` in ModelNew.py

## Related Pages

- **lang-ascendc-direct-launch-project** — compilable skeleton
- **lang-torch-npu-cpp-api** — C++ binding API
- **pattern-ascendc-compile-troubleshooting** — build error fixes
- **kernel-mkb-working-examples** — passing examples
