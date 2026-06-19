---
id: code-multikernelbench-ascendc-direct-launch
title: "MultiKernelBench — AscendC Direct Launch Backend"
type: source-code
repo: Agent4Kernel/MultiKernelBench
path: backends/ascendc_direct_launch_backend.py
url: https://github.com/Agent4Kernel/Agent4Kernel/tree/main/MultiKernelBench
source_category: upstream-code
architectures: [ascend910b]
tags: [ascendc, pybind, operator, tutorial, mkb]
date: '2026-06-19'
captured_at: '2026-06-19'
confidence: verified
hardware_features: [cube-unit, vector-unit, unified-buffer, mte]
techniques: [pipeline-scheduling, tiling-strategy]
kernel_types: [elementwise, matmul, activation]
languages: [ascendc, cpp, python]
---

# MultiKernelBench — AscendC Direct Launch Backend

Reference implementation for the `ascendc_direct_launch` evaluation backend used by MultiKernelBench (MKB). This is the canonical evidence for JSON submission format, auto-generated CMakeLists (bisheng), kernel vs binding source separation, and pybind11 + torch_npu integration.

## Code Location

- Repository: `Agent4Kernel/MultiKernelBench`
- Backend: `backends/ascendc_direct_launch_backend.py`
- Example JSON: `prompts/ascendc_direct_launch_model_add.json`
- Cheating detector: `utils/cheating_detection.py`
- Eval runner: `eval_single_runner.py`

## Key Files

| File | Purpose |
|------|---------|
| `ascendc_direct_launch_backend.py` | Parses JSON spec, writes sources, generates CMake, builds `.so`, loads `ModelNew` |
| `ascendc_direct_launch_model_add.json` | Minimal runnable Add example (kernel + pybind + ModelNew.py) |
| `cheating_detection.py` | AST-based detector for forbidden PyTorch compute in `forward()` |
| `eval_single_runner.py` | CLI wrapper producing `result.json` |

## Evidence: JSON Spec Shape

The backend expects a JSON object (not a markdown fence) with:

- `entry.model` — Python entry point, e.g. `"ModelNew.py::ModelNew"`
- `build.kernel_sources` — `.cpp` files compiled with `bisheng -xasc`
- `build.binding_sources` — host `.cpp` with `PYBIND11_MODULE`, linked by g++
- `build.module_name` — optional; inferred from `PYBIND11_MODULE` if omitted
- `sources[]` — embedded file contents keyed by relative path

See wiki page `lang-ascendc-direct-launch-project` for the full annotated template derived from this backend.
