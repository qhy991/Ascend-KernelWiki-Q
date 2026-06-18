---
id: doc-mindspore-ascendc-custom-op
title: "MindSpore AOT-Type AscendC Custom Operator Development"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [mindspore, ascendc, python, operator, aot]
date: '2026-03-05'
url: https://www.mindspore.cn/tutorials/en/master/custom_program/operation/op_custom_ascendc.html
hardware_features: [cube-unit, vector-unit, unified-buffer]
confidence: verified
---

# MindSpore AOT-Type AscendC Custom Operator Development

MindSpore tutorial describing how to wrap a pre-compiled AscendC operator as a Python-callable primitive via `ops.Custom` with `func_type="aot"`. The developer authors the operator in AscendC C++ (an `op_host/` definition and an `op_kernel/` implementation), compiles it into a vendor dynamic library, and then references that library from Python. This bridges the high-level MindSpore graph and the low-level AICore kernels documented in `kernel-matmul-ascendc` and `lang-ascendc-guide`.

## The `ops.Custom` Primitive

`ops.Custom` is the single entry point for custom operators. For AOT-type AscendC ops the full signature is:

```python
from mindspore import ops

custom_op = ops.Custom(
    func,                  # "aclnnAdd" or "./infer.cc:AddCustom"
    out_shape=None,        # output shape: tuple, or a Python infer callable
    out_dtype=None,        # output dtype, e.g. mstype.float16
    func_type="aot",       # AOT = ahead-of-time compiled AscendC op
    bprop=None,            # optional backward function for autograd
    reg_info=None,         # operator registration info (None -> inferred)
)
```

The `func` argument carries the binding. It may name a CANN aclnn entry such as `"aclnnAdd"`, or it may point at a C++ shape-inference symbol using the `"file.cc:OpName"` form, e.g. `"./infer.cc:AddCustom"`. The string before the colon is the source file containing the inference function; the string after is the operator name the runtime dispatches to.

## Workflow Overview

The AOT path has three stages, kept deliberately separate so the C++ kernel can be reused outside MindSpore.

| Stage | Artifact | Tooling |
|-------|----------|---------|
| 1. Author | `op_host/`, `op_kernel/` C++ | AscendC API (Cube / Vector / DataCopy) |
| 2. Compile | vendor dynamic library in `build_out` | `setup.py` packaging script |
| 3. Bind | Python primitive | `ops.Custom(..., func_type="aot")` |

### 1. Author the AscendC Sources

Two source trees are required:

- `op_host/` — the operator *definition*: tiling, shape/dtype registration, and workspace sizing that runs on the host CPU side (before the kernel is launched on the AICore).
- `op_kernel/` — the operator *implementation*: the AICore kernel body that issues Cube-unit, Vector-unit, and Unified Buffer operations.

This split mirrors the standard CANN custom-operator layout, so an operator developed for MindSpore can also be invoked from the ACL runtime without modification.

### 2. Compile to a Dynamic Library

The host and kernel sources are packaged with a `setup.py` script that invokes the CANN operator build. The key arguments are the two source paths, a vendor name, and the location of the installed CANN package:

```bash
python setup.py \
    --op_host_path={op_host_dir} \
    --op_kernel_path={op_kernel_dir} \
    --vendor_name=customize \
    --ascend_cann_package_path=/usr/local/Ascend/latest
```

A successful build emits a `build_out` directory containing the vendor operator package (a dynamic library plus its registration metadata). MindSpore loads this package at runtime when the bound `ops.Custom` primitive is first executed. The `--vendor_name` value (here `customize`) namespaces the operator so it does not collide with built-in CANN operators.

### 3. Bind from Python

Once `build_out` is on the operator search path, the primitive is constructed and called like any other MindSpore op:

```python
import mindspore as ms
from mindspore import ops, Tensor
import mindspore.common.dtype as mstype

# Bind the compiled AddCustom op; shape/dtype inferred in C++ infer.cc.
add_custom = ops.Custom(
    "./infer.cc:AddCustom",
    out_dtype=mstype.float16,
    func_type="aot",
)

x = Tensor([1.0, 2.0, 3.0], mstype.float16)
y = Tensor([4.0, 5.0, 6.0], mstype.float16)
out = add_custom(x, y)
```

## Shape and Dtype Inference

The output shape and dtype must be resolvable before the kernel launches. Two mechanisms are supported.

### Python Inference Callables

`out_shape` and `out_dtype` accept plain Python callables (or literal tuples/dtypes). This is the simplest option for ops whose output geometry is a direct function of the inputs — for example an element-wise op like the one in `kernel-elementwise-ascendc` simply returns its first input's shape.

### C++ Inference Function

For shape logic that should ship with the operator package, MindSpore supports a C++ inference function referenced through the `"file.cc:OpName"` form. The function uses the AOT extension ABI:

```cpp
// infer.cc — registered as "./infer.cc:AddCustom"
#include <vector>
#include <cstdint>

extern "C" std::vector<int64_t> AddCustomInferShape(
    int *ndims,          // rank of each input tensor
    int64_t **shapes,    // per-input shape arrays
    AotExtra *extra)     // attributes / workspace hooks
{
    // Element-wise: output shape == first input shape.
    std::vector<int64_t> out_shape;
    for (int i = 0; i < ndims[0]; ++i) {
        out_shape.push_back(shapes[0][i]);
    }
    return out_shape;
}
```

The function is declared `extern "C"` so the symbol name is stable for the `file.cc:OpName` lookup. `ndims[i]` gives the rank of input `i`, `shapes[i]` is that input's dimension array, and `AotExtra` exposes operator attributes and any host-side workspace requirements.

## Trade-offs and Pitfalls

- **Dynamic graph restriction**: In PyNative (dynamic) graph mode, AOT custom operators support only `Tensor` inputs and outputs. Scalar or list arguments must be folded into attributes at registration time or marshalled into tensors before the call.
- **Build environment coupling**: `--ascend_cann_package_path` must point at the CANN version the operator was authored against. A mismatch between the build-time CANN and the runtime CANN is the most common cause of load failures for `build_out` packages.
- **Vendor namespace**: Reusing a `--vendor_name` across two operator packages can shadow earlier registrations. Keep one vendor name per logical operator set.
- **Inference must be exact**: A wrong `out_shape`/`out_dtype` will not be caught by the kernel — it surfaces as a downstream allocation or correctness error, since the runtime trusts the inference result when sizing the output buffer.
- **Backward support is opt-in**: Autograd works only if a `bprop` function is supplied; otherwise the op is treated as non-differentiable.

## Comparison: AOT vs. Inline Custom Types

| Aspect | AOT (this page) | Pure-Python / pyfunc |
|--------|-----------------|----------------------|
| Implementation | AscendC C++ kernel | Python callable |
| Performance | AICore-native (Cube/Vector) | Interpreter-bound |
| Compilation | `setup.py` -> `build_out` | none |
| Best for | production kernels | prototyping / glue |

AOT is the right choice when the operator must run on the Cube and Vector units at full hardware throughput; the Python-callable types trade that performance for zero build steps. For authoring the underlying kernel body itself, see `lang-ascendc-guide`.

## Related Pages

- [AscendC Language Guide](lang-ascendc-guide) — authoring the `op_kernel/` body
- [AscendC API Reference](doc-ascendc-api-reference) — Cube / Vector / DataCopy primitives used in the kernel
- [MatMul Kernel](kernel-matmul-ascendc) — a Cube-unit kernel that can be wrapped as a custom op
- [Elementwise Kernel](kernel-elementwise-ascendc) — simple shape-inference example
