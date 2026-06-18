---
id: lang-mindspore-ascend-guide
title: "MindSpore on Ascend — AOT AscendC Custom Operators"
type: wiki-language
tags: [mindspore, ascendc, python, operator, aot]
confidence: source-reported
sources: [doc-mindspore-ascendc-custom-op, doc-ascendc-tiling-api]
architectures: [ascend910, ascend910b]
languages: [python, ascendc]
related: [lang-ascendc-guide, lang-pytorch-npu-guide]
---

## Overview

MindSpore is Huawei's deep-learning framework, and on Ascend NPUs it can call hand-written AscendC kernels through the `ops.Custom` primitive. The AOT (ahead-of-time) flavour of `ops.Custom` lets you ship a precompiled AscendC operator — an `op_host` tiling/prototype side plus an `op_kernel` device side — as a dynamic library and invoke it from Python inside an `nn.Cell`. This page covers the Python invocation surface, the compile command, and the two ways to supply shape inference; for the device kernel itself see lang-ascendc-guide, and for the host tiling that `op_host` implements see doc-ascendc-tiling-api.

## Where AOT Fits Among `func_type` Options

`ops.Custom` accepts several `func_type` values. AOT is the one that binds to a compiled AscendC operator rather than to interpreted Python or to a graph subexpression.

| `func_type` | What `func` points to | Device code | Typical use |
|-------------|-----------------------|-------------|-------------|
| `"aot"` | An installed operator symbol (e.g. `"aclnnAdd"`) or a built op | AscendC `op_host` + `op_kernel` | Custom or built-in AscendC operator |
| `"pyfunc"` | A Python callable | None (host) | Quick prototyping, debugging |
| `"akg"` | An AKG-generated kernel | Auto-generated | Auto-fused elementwise/reduce |

This page is exclusively about `func_type="aot"`, where the heavy lifting lives in AscendC and MindSpore only dispatches.

## The Two Halves of an AOT Operator

An AOT AscendC operator is split the same way as any AscendC operator project (the layout described in lang-ascendc-guide):

- **`op_host/`** — host C++: the operator prototype (shape and dtype inference, attribute registration) and the **tiling function**. The tiling function partitions the problem across AICores and fills the `TilingData` struct; the host-side tiling APIs it calls are documented in doc-ascendc-tiling-api.
- **`op_kernel/`** — the device-side AscendC kernel: the `Init()`/`Process()` class that reads `TilingData` and runs the CopyIn → Compute → CopyOut pipeline on the AICore.

MindSpore's AOT path consumes the compiled result of these two directories. It does not generate kernel code for you — you author it in AscendC and MindSpore calls the resulting symbol.

## Calling From Python — `ops.Custom`

The `func` argument selects the operator. It can name an already-installed operator symbol directly, or point at a source file plus a C++ inference function using the `./file.cc:FuncName` form.

```python
import mindspore as ms
from mindspore import nn, ops, Tensor

class AddCustomCell(nn.Cell):
    def __init__(self):
        super().__init__()
        # func_type="aot" binds to a compiled AscendC operator.
        # Option A: name an installed operator symbol directly.
        self.add = ops.Custom(
            func="aclnnAdd",
            out_shape=lambda x, y: x,        # Python-side shape infer
            out_dtype=lambda x, y: x,        # Python-side dtype infer
            func_type="aot",
        )

    def construct(self, x, y):
        # Invoked like any primitive inside the graph/cell.
        return self.add(x, y)

# Option B: C++-side shape inference via "./source.cc:Func".
add_cpp_infer = ops.Custom(
    func="./infer.cc:AddCustom",         # AddCustomInferShape lives in infer.cc
    out_shape=None,                      # None => use the C++ infer function
    out_dtype=ms.float16,
    func_type="aot",
)
```

Both `out_shape` and `out_dtype` may be a concrete value, a Python lambda over the input shapes/dtypes, or `None` to defer to the C++ inference function named in `func`.

### Python-side vs. C++-side Shape Inference

| Aspect | Python-side (`out_shape=lambda ...`) | C++-side (`func="./infer.cc:AddCustom"`) |
|--------|--------------------------------------|------------------------------------------|
| Where it runs | Host, in the Python tracer | Compiled `AddCustomInferShape` in the op |
| What you write | A lambda over input shapes | A C++ `InferShape` registered in `op_host` |
| Best for | Simple, static, elementwise shapes | Reused logic, complex/data-dependent shapes |
| Graph-mode compatibility | Fine for static shapes | Preferred for ops shipped as a package |

For an elementwise add the output shape equals the input shape, so the Python lambda `lambda x, y: x` is sufficient. When the same inference logic ships with the operator package (the `AddCustomInferShape` registered in `op_host`), point `func` at the `.cc` file and set `out_shape=None` so MindSpore calls the compiled inference instead.

## Compiling the Operator to a Dynamic Library

The `op_host` and `op_kernel` sources are compiled and packaged with `setup.py`. The build links the AscendC kernel, compiles the host tiling/prototype, and installs a vendor-named custom operator package that MindSpore's AOT path can discover.

```bash
python setup.py \
    --op_host_path=./op_host \
    --op_kernel_path=./op_kernel \
    --vendor_name=customize \
    --ascend_cann_package_path=/usr/local/Ascend/ascend-toolkit/latest
```

- `--op_host_path` / `--op_kernel_path` point at the two source directories described above.
- `--vendor_name=customize` namespaces the installed operator so it does not collide with vendor or built-in operators.
- `--ascend_cann_package_path` is the CANN toolkit root used to resolve the AscendC headers and the host tiling APIs (doc-ascendc-tiling-api).

After the package installs, the operator symbol named in `ops.Custom(func=...)` becomes resolvable and the `nn.Cell` above can run on the NPU.

## End-to-End Flow

1. **Author** `op_host/` (prototype + tiling, per doc-ascendc-tiling-api) and `op_kernel/` (the AscendC kernel, per lang-ascendc-guide).
2. **Write** the C++ shape-inference function (e.g. `AddCustomInferShape`) if you want C++-side inference.
3. **Compile** with the `setup.py` command above, producing the `--vendor_name` custom operator package.
4. **Declare** the operator in Python with `ops.Custom(func=..., out_shape=..., out_dtype=..., func_type="aot")`.
5. **Call** it inside `Cell.construct`, where it behaves like any other primitive.

## Trade-offs, Pitfalls, and Notes

- **AOT means precompiled.** `func_type="aot"` does not compile AscendC for you at runtime — the operator must already be built and installed via `setup.py`. A missing or stale package surfaces as an unresolved operator at graph build time.
- **`out_shape=None` requires C++ inference.** If you set `out_shape=None` but `func` does not name a `.cc:Func` inference (e.g. `./infer.cc:AddCustom`), MindSpore has no way to infer the output shape and dispatch fails. Provide either the lambda or the C++ inference, not neither.
- **Vendor name must match at call time.** The `--vendor_name` used at compile time namespaces the installed operator; pointing `ops.Custom` at a symbol under a different vendor namespace will not resolve.
- **Tiling lives in `op_host`, not Python.** Do not try to reproduce tiling logic in the Python lambdas — the lambdas only infer output metadata. The actual AICore partitioning is the `op_host` tiling function (doc-ascendc-tiling-api); Python shape inference and host tiling are separate concerns.
- **CANN package path must match the runtime.** `--ascend_cann_package_path` should point at the same CANN toolkit version the device driver expects; a mismatch can compile a package that fails to load.
- **Static shapes are smoothest in graph mode.** Python-side lambda inference works cleanly for static elementwise shapes; for dynamic or data-dependent shapes, prefer the C++ inference shipped in the package.

## Where This Fits

Use the MindSpore AOT path when you already have (or are willing to author) an AscendC operator and want to call it from MindSpore Python inside an `nn.Cell`. The device kernel authoring is covered in lang-ascendc-guide and the host tiling it depends on is in doc-ascendc-tiling-api. For invoking comparable hand-written kernels from the PyTorch side of Ascend, see lang-pytorch-npu-guide.
