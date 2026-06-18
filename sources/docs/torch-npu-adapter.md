---
id: doc-torch-npu-adapter
title: "torch_npu — PyTorch Ascend Adapter and Custom Operator Registration"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [torch-npu, pytorch, python, cpp, operator]
date: '2026-04-01'
url: https://github.com/Ascend/pytorch
hardware_features: [cube-unit, vector-unit]
confidence: verified
---

# torch_npu — PyTorch Ascend Adapter

`torch_npu` is the out-of-tree adapter that brings Ascend NPU support to PyTorch without forking the core framework. It registers the NPU as a PrivateUse1 backend, exposes it through the device string `"npu"`, and ships a library of Ascend-optimized operators (including fused kernels like `npu_fusion_attention`) that dispatch onto the AICore Cube and Vector units. The package is the foundation that inference engines such as vLLM-Ascend and SGLang's NPU path build upon.

## Backend Model: PrivateUse1

PyTorch reserves a generic backend dispatch key, `PrivateUse1`, for out-of-tree accelerators. `torch_npu` claims this key and renames it to `npu`, so existing PyTorch code works with minimal changes — you move tensors with `tensor.npu()` or `tensor.to("npu")` exactly as you would with `.cuda()`.

```python
import torch
import torch_npu  # registers the PrivateUse1 backend as "npu"

# Tensors and modules move to the NPU just like CUDA
x = torch.randn(4096, 4096, dtype=torch.float16).npu()
w = torch.randn(4096, 4096, dtype=torch.float16).to("npu")

# Standard ops dispatch onto AICore via the registered backend
y = torch.matmul(x, w)
print(y.device)   # npu:0
```

Importing `torch_npu` is mandatory and must follow `import torch`; the import side-effect is what wires the dispatch key, registers the device guard, and installs the allocator and stream implementations backed by ACL (the Ascend Computing Language runtime).

## Operator Plumbing: op_plugin and codegen

The operator layer lives in **op_plugin**, which holds the actual Ascend kernel implementations, and a **codegen** step that wires those implementations into PyTorch's dispatcher. The contract between the two is a YAML manifest, `npu_native_functions.yaml`, which enumerates every operator the adapter supports and how it should be registered.

The flow is:

1. An operator schema is declared in `npu_native_functions.yaml` (name, signature, dispatch target).
2. `codegen` reads the YAML and emits C++ dispatcher registration code, binding each schema to its op_plugin implementation under the `PrivateUse1` / `npu` key.
3. The generated registrations are compiled into the adapter so the op is reachable through the normal PyTorch dispatch path.

```yaml
# npu_native_functions.yaml (excerpt)
official:
  - func: npu_rms_norm(Tensor self, Tensor gamma, float epsilon=1e-6) -> (Tensor, Tensor)
  - func: npu_fusion_attention(Tensor query, Tensor key, Tensor value, int head_num, str input_layout, *, Tensor? atten_mask=None, float scale=1.0, float keep_prob=1.0) -> (Tensor, Tensor, Tensor, Tensor, int, int, int)
```

This codegen approach keeps the operator surface declarative: adding a new op is mostly a matter of adding a YAML entry plus its op_plugin kernel, rather than hand-writing dispatcher boilerplate.

## Native Fused Operators

Beyond plain elementwise and GEMM coverage, `torch_npu` exposes hand-tuned fused operators in the `torch_npu` namespace. These collapse multiple stages into a single AICore launch, cutting Unified Buffer round-trips and keeping the Cube and Vector units busy.

```python
import torch
import torch_npu

hidden = torch.randn(8, 4096, 8192, dtype=torch.float16).npu()
gamma = torch.ones(8192, dtype=torch.float16).npu()

# Fused RMSNorm — returns (output, rstd)
out, rstd = torch_npu.npu_rms_norm(hidden, gamma, epsilon=1e-6)

# Fused attention (FlashAttention-style) on the Cube + Vector pipeline
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

For the underlying matrix-multiply techniques these fused ops rely on, see `kernel-matmul-ascendc`; the quantization path in `npu_quant_matmul` connects to the material in `doc-ascend-quantization-guide`.

## Custom Operator Registration

When the built-in operators are not enough, you can write your own AscendC kernel and surface it as a PyTorch op. The kernel is compiled from AscendC source via a `CMakeLists.txt` build, then bound into PyTorch through the `TORCH_LIBRARY` / `torch.library` mechanism.

The C++ binding side declares a library namespace and attaches the implementation under the `PrivateUse1` (npu) key:

```cpp
#include <torch/library.h>

at::Tensor my_add_npu(const at::Tensor& a, const at::Tensor& b);

// Declare the schema in a custom namespace
TORCH_LIBRARY(my_ops, m) {
    m.def("my_add(Tensor a, Tensor b) -> Tensor");
}

// Bind the AscendC-backed implementation to the npu backend
TORCH_LIBRARY_IMPL(my_ops, PrivateUse1, m) {
    m.impl("my_add", &my_add_npu);
}
```

The AscendC kernel itself is compiled by CMake against the CANN toolkit and linked into the extension. From Python the op is then callable through `torch.ops`:

```python
import torch
import torch_npu
import my_ops_ext  # extension module exporting the TORCH_LIBRARY bindings

a = torch.randn(1024, dtype=torch.float16).npu()
b = torch.randn(1024, dtype=torch.float16).npu()
c = torch.ops.my_ops.my_add(a, b)
```

`torch.library` (the Python-side API) can also register fake/meta implementations for shape inference and autograd formulas, which is what lets custom ops participate in `torch.compile` graphs and tracing.

## Repository Layout and Mirrors

The canonical source is the Ascend `pytorch` repository, with maintained mirrors on Gitee and GitCode under the same `Ascend/pytorch` path for users behind the Great Firewall. The repository version is pinned against a specific upstream PyTorch release and a matching CANN toolkit version — mismatches between the three are the most common source of import failures.

| Component | Role |
| --- | --- |
| PyTorch (upstream) | Core framework, provides `PrivateUse1` dispatch key |
| `torch_npu` adapter | Backend registration, allocator, streams, op_plugin |
| CANN toolkit | ACL runtime + AscendC compiler the kernels build against |

## Trade-offs and Pitfalls

- **Import order matters.** `import torch_npu` must come after `import torch`. Reversing them, or forgetting the import entirely, leaves the `npu` device unregistered and `.npu()` calls fail.
- **Version triple coupling.** The PyTorch version, the `torch_npu` adapter version, and the CANN toolkit version must be mutually compatible. A wrong CANN version typically surfaces as an opaque ACL initialization error at first NPU op, not at import.
- **Not every op is fused.** Operators absent from `npu_native_functions.yaml` fall back to generic decompositions, which may issue many small AICore launches and underutilize the Cube unit. Profiling (see `doc-ascend-profiling-guide`) is the way to confirm an op is taking the fused path.
- **Custom op build dependencies.** Building a custom AscendC op requires the CANN toolkit and its CMake config on the build machine; the extension must be compiled against the same CANN version as the installed `torch_npu`.
- **PrivateUse1 is single-occupant.** Only one out-of-tree backend can claim `PrivateUse1` per process, so `torch_npu` cannot coexist with another adapter that also grabs that key.

## Downstream Usage

`torch_npu` is the integration point for higher-level inference stacks. vLLM-Ascend uses it to run the model graph and to reach fused kernels like `npu_fusion_attention` for its attention backend, and SGLang's NPU path relies on the same adapter for device placement and fused operators. In both cases the engine layers its own scheduling and KV-cache management on top of the operator surface that `torch_npu` provides.

## Status

Verified against the Ascend `pytorch` adapter. Backend is registered as the `npu` (PrivateUse1) device; native fused ops `npu_rms_norm`, `npu_fusion_attention`, `npu_rotary_mul`, and `npu_quant_matmul` are part of the op_plugin operator set. Custom AscendC operators are supported through `TORCH_LIBRARY` / `torch.library` bindings.
