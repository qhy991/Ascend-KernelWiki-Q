---
id: lang-pytorch-npu-guide
title: "PyTorch on Ascend — torch_npu, Custom Kernels, and Bindings"
type: wiki-language
tags: [torch-npu, pytorch, python, cpp, operator]
confidence: source-reported
sources: [doc-torch-npu-adapter, doc-vllm-ascend, pr-vllm-ascend-001]
architectures: [ascend910, ascend910b]
languages: [python, cpp]
related: [lang-ascendc-guide, migration-pytorch-cuda-to-npu, lang-torch-npu-cpp-api, lang-ascendc-direct-launch-project, lang-mkb-integration-rules]
---

## Overview

`torch_npu` is the out-of-tree adapter that brings Ascend NPU support to PyTorch without forking the core framework. It registers the NPU as PyTorch's generic `PrivateUse1` backend, exposes it through the device string `"npu"`, and ships a library of Ascend-optimized operators — including fused kernels like `npu_fusion_attention` — that dispatch onto the AICore Cube and Vector units. This page is the Python-facing entry point: how to install and import the adapter, how tensors and modules move to the device, which native fused ops to reach for, and how to surface your own AscendC kernel (see lang-ascendc-guide) as a regular `torch.ops` call.

## Install and Import

The single hard rule is import order: `import torch_npu` **must follow** `import torch`. The import is a side-effect — it wires the `PrivateUse1` dispatch key, registers the device guard, and installs the allocator and stream implementations backed by the ACL runtime. Reverse the order, or forget the import, and the `npu` device is simply never registered.

```python
import torch
import torch_npu          # registers the PrivateUse1 backend as "npu"

print(torch.npu.is_available())   # True on a configured Ascend host
print(torch.npu.device_count())   # number of visible AICore devices
```

The PyTorch version, the `torch_npu` adapter version, and the CANN toolkit version form a coupled triple; a mismatched CANN usually surfaces as an opaque ACL initialization error at the *first* NPU op rather than at import. The canonical source is the Ascend `pytorch` repository, with maintained Gitee and GitCode mirrors under the same path.

## The "npu" Device (PrivateUse1)

PyTorch reserves `PrivateUse1` as a generic dispatch key for out-of-tree accelerators. `torch_npu` claims it and renames it `npu`, so code written for CUDA ports with minimal changes — `.cuda()` becomes `.npu()` and `"cuda"` becomes `"npu"`. The end-to-end porting story is covered in migration-pytorch-cuda-to-npu; the essentials are below.

```python
import torch
import torch_npu

# Move tensors and modules to the NPU just like CUDA
x = torch.randn(4096, 4096, dtype=torch.float16).npu()
w = torch.randn(4096, 4096, dtype=torch.float16).to("npu")

# Standard ops dispatch onto AICore via the registered backend
y = torch.matmul(x, w)          # GEMM lands on the Cube unit
print(y.device)                  # npu:0
```

| CUDA idiom | Ascend (`torch_npu`) equivalent |
| --- | --- |
| `import torch` | `import torch` **then** `import torch_npu` |
| `tensor.cuda()` | `tensor.npu()` |
| `tensor.to("cuda")` | `tensor.to("npu")` |
| `torch.cuda.is_available()` | `torch.npu.is_available()` |
| `torch.cuda.synchronize()` | `torch.npu.synchronize()` |
| dispatch key `CUDA` | dispatch key `PrivateUse1` (surfaced as `npu`) |

Only one out-of-tree backend can claim `PrivateUse1` per process, so `torch_npu` cannot coexist with another adapter that also grabs that key.

## Mixed Precision and bf16

Dense layers (attention projections, MLP GEMMs) run on the Cube unit, which is at its best in 16-bit. Both FP16 and BF16 are first-class on Ascend 910B, and autocast follows the standard PyTorch surface with `"npu"` as the device type.

```python
import torch
import torch_npu

model = build_model().npu()
scaler = torch.npu.amp.GradScaler()

for inputs, target in loader:
    inputs, target = inputs.npu(), target.npu()
    with torch.autocast(device_type="npu", dtype=torch.bfloat16):
        out = model(inputs)
        loss = loss_fn(out, target)
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

BF16 avoids the loss-scaling fragility of FP16 (its wider exponent range tolerates large gradients) at the cost of fewer mantissa bits; FP16 keeps more precision but typically needs a `GradScaler`. Pick per workload.

## Native Fused Operators

Beyond plain elementwise and GEMM coverage, `torch_npu` exposes hand-tuned fused operators in the `torch_npu` namespace. Each collapses several stages into a single AICore launch, cutting Unified Buffer round-trips and keeping the Cube and Vector units busy — the same operator surface that inference engines like vLLM-Ascend (doc-vllm-ascend) build on.

```python
import torch
import torch_npu

hidden = torch.randn(8, 4096, 8192, dtype=torch.float16).npu()
gamma  = torch.ones(8192, dtype=torch.float16).npu()

# Fused RMSNorm — returns (output, rstd)
out, rstd = torch_npu.npu_rms_norm(hidden, gamma, epsilon=1e-6)

# Fused FlashAttention-style attention on the Cube + Vector pipeline
q = torch.randn(1, 32, 2048, 128, dtype=torch.float16).npu()
k = torch.randn(1, 32, 2048, 128, dtype=torch.float16).npu()
v = torch.randn(1, 32, 2048, 128, dtype=torch.float16).npu()
attn = torch_npu.npu_fusion_attention(
    q, k, v, head_num=32, input_layout="BNSD", scale=0.0883
)[0]
```

| Native op | Purpose | Fuses |
| --- | --- | --- |
| `npu_rms_norm` | RMS normalization | square-mean reduce + rsqrt + scale |
| `npu_fusion_attention` | FlashAttention-style attention | QK^T + scale + softmax + AV |
| `npu_rotary_mul` | Rotary position embedding | cos/sin gather + complex rotate |
| `npu_quant_matmul` | Quantized matrix multiply | INT8 GEMM + dequant scale |

Operators *absent* from the adapter's `npu_native_functions.yaml` manifest fall back to generic decompositions, which may issue many small AICore launches and underutilize the Cube unit. Confirming an op took the fused path is a profiling question, not an assumption. For the matrix-multiply techniques these fused ops rely on, see kernel-matmul-ascendc.

## Adding a Custom AscendC Kernel

When the built-in operators are not enough, you write your own AscendC kernel and surface it as a PyTorch op. The path mirrors the worked example in pr-vllm-ascend-001 (vllm-ascend's `rotary_embedding`, PR #371): compile the AscendC source with CMake against the CANN toolkit, bind it into PyTorch with `TORCH_LIBRARY`, and call it from Python through `torch.ops`. There are four stages.

### 1. Write the device kernel (`op_kernel`, AscendC)

The kernel is an ordinary AscendC operator — a class with `Init()`/`Process()` and a `__global__ __aicore__` entry point — described in detail in lang-ascendc-guide. It runs on the AICore and is the only device-side code you write.

### 2. Compile via CMake against CANN

A `CMakeLists.txt` invokes the Ascend compiler toolchain (the CANN `ascendc` CMake helpers) to turn each `.cpp` kernel into a device object linked into the extension `.so`. The extension must be built against the **same** CANN version as the installed `torch_npu`.

### 3. Bind with `TORCH_LIBRARY` (host C++)

The host binding declares a schema in a custom namespace and attaches the AscendC-backed implementation under the `PrivateUse1` (npu) key. Registering under the wrong dispatch key silently routes calls back to the framework op and erases any speedup.

```cpp
// torch_binding.cpp
#include <torch/library.h>

// AscendC-backed implementation, compiled via CMake against CANN.
std::tuple<at::Tensor, at::Tensor> rotary_embedding_npu(
    const at::Tensor& query, const at::Tensor& key,
    const at::Tensor& cos,   const at::Tensor& sin, int64_t rot_dim);

TORCH_LIBRARY(_C, m) {
  m.def("rotary_embedding(Tensor query, Tensor key, "
        "Tensor cos, Tensor sin, int rot_dim) -> (Tensor, Tensor)");
}

TORCH_LIBRARY_IMPL(_C, PrivateUse1, m) {   // PrivateUse1 == "npu"
  m.impl("rotary_embedding", &rotary_embedding_npu);
}
```

### 4. Call from Python via `torch.ops`

Importing the compiled extension runs the `TORCH_LIBRARY` registration; the op is then a normal `torch.ops.<namespace>.<op>` callable on `npu` tensors.

```python
import torch
import torch_npu
import vllm_ascend._C          # import side-effect registers the TORCH_LIBRARY ops

# query / key live on device "npu"; dispatch lands on rotary_embedding_npu
q, k = torch.ops._C.rotary_embedding(query, key, cos, sin, rot_dim)
```

`torch.library` (the Python-side API) can additionally register fake/meta implementations for shape inference, which is what lets a custom op participate in `torch.compile` graphs and tracing.

## Worked Example: vLLM-Ascend `rotary_embedding`

pr-vllm-ascend-001 is the canonical end-to-end reference for this path. PR #371 adds the CMake scaffolding that compiles AscendC `.cpp` sources and registers them through `torch_library`, landing `rotary_embedding` as the first custom kernel. The motivation is specific to serving: RoPE fires on query and key *every* decode step, so routing it through generic framework ops accumulates dispatch overhead and Unified Buffer round-trips. The custom kernel fuses the cos/sin gather with the rotate-half application in a single Vector-unit pass, keeping intermediates UB-resident.

The follow-up optimization (issue #802) reports up to **9.36x** and **8.26x** speedups for the kernel versus the reference rotary path on Ascend 910B. Two caveats from the source: these are **kernel-level** comparisons (not whole-model throughput), and they are for **specific shapes/cases** — a hand-tuned kernel only wins on the tiling regimes it was tuned for. The same pattern carries vllm-ascend's vocab-parallel embedding (PR #796) and multi-step prepare-input (PR #814).

## Native Op vs. Custom Kernel

| Aspect | Native fused op (`torch_npu.*`) | Custom AscendC op (`torch.ops.*`) |
| --- | --- | --- |
| Who writes it | Ships with the adapter | You author the AscendC kernel |
| Where it runs | AICore (Cube/Vector) | AICore (Cube/Vector) |
| Build dependency | None — already installed | CMake + CANN toolkit at build time |
| Call site | `torch_npu.npu_xxx(...)` | `torch.ops.<ns>.<op>(...)` |
| When to use | An existing fused op fits | No op covers a genuinely hot path |
| Maintenance | Maintained upstream | Must track CANN + dispatcher changes |

## Trade-offs, Pitfalls, and Notes

- **Import order is non-negotiable.** `import torch_npu` after `import torch`, every time. Reversing or omitting it leaves `npu` unregistered and `.npu()` calls fail.
- **Version triple coupling.** PyTorch, `torch_npu`, and CANN must be mutually compatible. A wrong CANN version typically surfaces as an opaque ACL error at the first NPU op, not at import.
- **Not every op is fused.** Ops outside `npu_native_functions.yaml` decompose into many small launches and underutilize the Cube unit; profile to confirm the fused path.
- **`PrivateUse1` is single-occupant.** Only one out-of-tree backend per process — `torch_npu` cannot share the key with another adapter.
- **Custom-op dispatch key.** A custom op must register under `PrivateUse1` (`npu`); the wrong key silently falls back to the framework op and erases the speedup.
- **Custom-op build chain.** Building an AscendC op needs the CANN toolkit and its CMake config, compiled against the same CANN version as the installed `torch_npu`.
- **Reported speedups are kernel-level and shape-specific.** The 9.36x / 8.26x `rotary_embedding` figures (pr-vllm-ascend-001) are per-kernel and per-shape, not end-to-end; always validate your actual decode shapes.

## Where This Fits

Use `torch_npu` whenever you want PyTorch model code to run on Ascend: move tensors with `.npu()`, reach for native fused ops like `npu_fusion_attention` where they exist, and drop down to a custom AscendC kernel only for genuinely hot paths. For authoring the device-side kernel, see lang-ascendc-guide; for porting an existing CUDA model end-to-end, see migration-pytorch-cuda-to-npu; and for a complete worked custom-op example, see pr-vllm-ascend-001 and the broader plugin context in doc-vllm-ascend.
