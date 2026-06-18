---
id: lang-tik-guide
title: "TIK — Low-Level Python Kernel Programming (Tensor Iterator Kernel)"
type: wiki-language
tags: [tbe-tik, tik, python, operator]
confidence: source-reported
sources: [doc-tik-api-reference, blog-tik-operator-walkthrough, doc-cann-architecture-guide]
architectures: [ascend910, ascend910b, ascend310p]
languages: [tbe-tik, python]
related: [lang-tbe-dsl-guide, lang-ascendc-guide, kernel-add-tik]
---

## Overview

TIK (Tensor Iterator Kernel) is a Python-based, host-side DSL within TBE for hand-writing custom operators on the Ascend AI Core. The host Python is not the kernel — it is a builder that constructs an in-memory instruction stream and then compiles that stream through the TBE/TVM stack into an AI Core binary. TIK exposes the memory hierarchy and the vector/MTE instruction set directly, while still automating Unified Buffer address allocation and read/write dependency tracking.

In the Ascend DSL spectrum, TIK occupies the middle. It is **lower-level than TBE-DSL** (see `lang-tbe-dsl-guide`), which auto-schedules from a declarative compute expression, and **higher-level than AscendC C++** (see `lang-ascendc-guide`), which exposes raw queues and pipeline sync events. TIK is imperative Python where you control scope placement, tiling, and instruction selection — but the compiler still plans buffers and orders instructions for you.

| Aspect | TBE-DSL | TIK | AscendC |
|--------|---------|-----|---------|
| Language | Python (declarative) | Python (imperative) | C/C++ |
| Buffer addressing | Automatic | Automatic | Manual (TPipe/TQue) |
| Instruction ordering | Automatic | Automatic (dep graph) | Manual + sync events |
| Tiling / mask / stride | Automatic | Manual | Manual |
| Status | Deprecated | Legacy / deprecated | Recommended |

## Programming Model

A TIK kernel is built by instantiating a `Tik` container, declaring tensors in named memory scopes, moving data between Global Memory and the Unified Buffer, issuing vector/reduce instructions over on-chip tensors, and finally compiling. Control-flow constructs such as `for_range` expand into *device-side* loops rather than executing in Python.

```python
from te import tik

tik_instance = tik.Tik()
```

Tensors are declared with `tik_instance.Tensor(dtype, shape, name, scope)`. The `scope` argument is the key control surface, binding the tensor to a physical memory:

| Scope constant   | Physical memory          | Typical use                                 |
|------------------|--------------------------|---------------------------------------------|
| `tik.scope_gm`   | Global Memory (HBM/DDR)  | Kernel inputs/outputs, host-visible buffers |
| `tik.scope_ubuf` | Unified Buffer (UB)      | Working set for vector/reduce compute       |
| `tik.scope_cbuf` | L1 Buffer                | Staging for matrix/feature-map reuse        |

Vector and reduce instructions operate on `scope_ubuf` tensors only; data must first be staged into the UB via an explicit `data_move`. Declaring a tensor does not by itself emit a copy.

## Data Movement

`tik_instance.data_move(dst, src, sid, nburst, burst_len, src_stride, dst_stride)` is the MTE-backed transfer primitive used for GM↔UB (and UB↔L1) copies:

- `sid` — reserved channel/sync id, normally `0`.
- `nburst` — number of bursts (contiguous fragments) to transfer.
- `burst_len` — length of each burst **in 32-byte units**.
- `src_stride` / `dst_stride` — gap (in 32-byte units) between consecutive bursts, enabling strided/gather-style movement.

A single `data_move` with `nburst=1` and a `burst_len` covering the whole tensor performs a plain contiguous copy; a larger `nburst` with non-zero strides expresses tiled or interleaved transfers without manual address arithmetic.

## Vector Compute

Vector instructions execute on the Vector unit over UB-resident tensors. They share a common shape: an explicit `mask` (elements processed per repeat), a `repeat_times` count, and per-operand block/repeat strides that let one call sweep a large tensor.

```python
# vec_<op>(mask, dst, src0[, src1], repeat_times,
#          dst_blk_stride, src0_blk_stride[, src1_blk_stride],
#          dst_rep_stride, src0_rep_stride[, src1_rep_stride])

tik_instance.vec_add(128, dst_ub, a_ub, b_ub, 8, 1, 1, 1, 8, 8, 8)  # elementwise add
tik_instance.vec_mul(128, dst_ub, a_ub, b_ub, 8, 1, 1, 1, 8, 8, 8)  # elementwise multiply
tik_instance.vec_max(128, dst_ub, a_ub, b_ub, 8, 1, 1, 1, 8, 8, 8)  # elementwise maximum
tik_instance.vec_exp(128, dst_ub, src_ub, 8, 1, 1, 8, 8)            # exp() (single source)
```

For axis reductions, `vec_reduce_*` collapse a UB tensor into a scalar (or per-repeat) result. A scratch UB tensor (`work_ub`) is passed for cross-repeat accumulation:

```python
tik_instance.vec_reduce_add("float16", dst_ub, src_ub, work_ub, repeat_times, src_rep_stride)
tik_instance.vec_reduce_max("float16", dst_ub, src_ub, work_ub, repeat_times, src_rep_stride)
```

A numerically stable softmax is the canonical composite: `vec_reduce_max` for the per-row maximum, `vec_sub` + `vec_exp` for the shifted numerators, `vec_reduce_add` for the denominator, and `vec_rec` of the denominator before the final multiply. All operands must reside in `scope_ubuf`.

## Control Flow and Double Buffering

`for_range` expands into a device-side loop. Passing `thread_num=2` enables ping-pong (double-buffered) execution: TIK automatically allocates two UB sub-buffers and overlaps the `data_move` of the next tile with compute on the current tile, hiding MTE latency behind the Vector unit. With `thread_num=1` the loop is single-buffered.

## Complete Example — Tiled, Double-Buffered Vector Add

This full kernel adds two 1024-element fp16 vectors, tiling the input across an 8-iteration loop with `thread_num=2` so the framework allocates ping-pong UB buffers automatically. See `kernel-add-tik` for the operator-packaging walkthrough that wraps this in a custom-op plugin.

```python
from te import tik

def vector_add(kernel_name="vector_add"):
    tik_instance = tik.Tik()

    total = 1024
    tile = 128
    loops = total // tile  # 8

    # Global Memory tensors (host-visible I/O)
    x_gm = tik_instance.Tensor("float16", (total,), name="x_gm", scope=tik.scope_gm)
    y_gm = tik_instance.Tensor("float16", (total,), name="y_gm", scope=tik.scope_gm)
    z_gm = tik_instance.Tensor("float16", (total,), name="z_gm", scope=tik.scope_gm)

    # thread_num=2 -> double-buffered (ping-pong) UB allocation
    with tik_instance.for_range(0, loops, thread_num=2) as i:
        x_ub = tik_instance.Tensor("float16", (tile,), name="x_ub", scope=tik.scope_ubuf)
        y_ub = tik_instance.Tensor("float16", (tile,), name="y_ub", scope=tik.scope_ubuf)
        z_ub = tik_instance.Tensor("float16", (tile,), name="z_ub", scope=tik.scope_ubuf)

        # GM -> UB (burst_len in 32-byte units: 128 fp16 = 256 B = 8 blocks)
        tik_instance.data_move(x_ub, x_gm[i * tile], 0, 1, tile // 16, 0, 0)
        tik_instance.data_move(y_ub, y_gm[i * tile], 0, 1, tile // 16, 0, 0)

        # Compute on the Vector unit (mask=128 covers a full fp16 vector, 1 repeat)
        tik_instance.vec_add(tile, z_ub, x_ub, y_ub, 1, 1, 1, 1, 8, 8, 8)

        # UB -> GM
        tik_instance.data_move(z_gm[i * tile], z_ub, 0, 1, tile // 16, 0, 0)

    tik_instance.BuildCCE(kernel_name=kernel_name,
                          inputs=[x_gm, y_gm], outputs=[z_gm])
    return tik_instance
```

## Compilation

`tik_instance.BuildCCE(kernel_name, inputs, outputs)` lowers the accumulated instruction stream through TBE/TVM into a `.o`/`.json` operator package for the target AI Core. The `inputs` and `outputs` lists bind `scope_gm` tensors to the kernel's external signature. The resulting object is wrapped in a custom-op plugin for registration with the CANN runtime (see `doc-cann-architecture-guide` for where this sits in the operator toolchain).

## When to Use TIK vs. AscendC

| Use TIK when… | Use AscendC when… |
|---------------|-------------------|
| Maintaining or extending a legacy TBE custom op | Authoring any new operator |
| A MindSpore aot custom kernel already targets TIK | You need Ascend910B Cube/feature support |
| You want Python-side codegen with auto buffer planning | You need maximum control and best performance |
| The schedule is vector/MTE-bound and modest in scope | The kernel is matrix-heavy or fusion-critical |

For new development the modern successor is AscendC; see `lang-ascendc-guide` for the C++ class-based model (`Init`/`Process`, `TPipe`/`TQue`, `DataCopy`, `Add`) that replaces the TIK surface. For the higher-level declarative path TIK descended from, see `lang-tbe-dsl-guide`. Matrix-heavy kernels are better expressed through the Cube path in AscendC rather than the TIK vector/MTE surface.

## Trade-offs and Pitfalls

- **Deprecated direction**: TIK is superseded by AscendC for new development. It still appears in legacy custom operators and in some MindSpore aot kernels, but new kernels should target AscendC.
- **Python overhead**: the builder runs entirely on the host as ordinary Python, and the TBE/TVM lowering path adds compilation latency; the abstraction sits on a fragile TVM-based toolchain (a key reason AscendC replaced TBE — see `lang-tbe-dsl-guide`).
- **Mask vs. shape mismatch**: `mask` counts elements processed per repeat, not bytes; for fp16 a full vector is 128 elements. A `mask`/`repeat_times` product that under- or over-covers the tensor silently processes the wrong range.
- **Stride units are 32-byte blocks**: `burst_len` and the stride arguments in `data_move` are in 32-byte units, not elements — a frequent source of off-by-N transfer bugs.
- **Scope discipline**: vector and reduce instructions reject `scope_gm` operands; forgetting a `data_move` into `scope_ubuf` is a common error.
- **Double-buffer UB pressure**: `thread_num=2` doubles the live UB footprint of loop-body tensors; oversized tiles can exhaust the Unified Buffer.

## Notes

- TIK frees the developer from hand-computing UB addresses and pipeline sync events, but performance still hinges on developer-chosen tiling, mask, stride, and double buffering.
- Tensors and loops lower to TVM IR before final code generation; this is the same TBE/TVM stack TBE-DSL is built on.
- Per the `source-reported` confidence of this page, the API names and behavior above reflect the documented TIK surface; no benchmark figures are asserted here.
