---
id: doc-tik-api-reference
title: "TIK (Tensor Iterator Kernel) Python API Reference"
type: source-doc
architectures: [ascend910, ascend910b, ascend310p]
tags: [tbe-tik, tik, python, operator, cann]
date: '2025-09-10'
url: https://support.huaweicloud.com/intl/en-us/TBEdevg-cann202training1/atlaste_10_0050.html
hardware_features: [unified-buffer, vector-unit, mte, global-memory]
techniques: [double-buffering, data-reuse]
confidence: verified
---

TIK (Tensor Iterator Kernel) is a Python-based, host-side DSL for authoring custom operators on the Ascend AI Core. A TIK program runs entirely on the host as ordinary Python: it builds an in-memory representation of the kernel and then compiles that representation — through the underlying TBE/TVM stack — into an Ascend AI Core binary. TIK sits at a lower abstraction level than graph-mode operators, exposing the memory hierarchy and vector/MTE instructions directly while still automating dependency tracking and buffer planning.

## Programming Model

A TIK kernel is described by instantiating a `Tik` container, declaring tensors in named memory scopes, moving data between Global Memory and the Unified Buffer, issuing vector/reduce instructions over on-chip tensors, and finally compiling the result. The host-side Python is *not* the kernel — it is a builder that emits the instruction stream. Control-flow constructs such as `for_range` likewise expand into device loops rather than executing in Python.

```python
from te import tik

tik_instance = tik.Tik()

# Global Memory tensors (host-visible I/O)
x_gm = tik_instance.Tensor("float16", (1024,), name="x_gm", scope=tik.scope_gm)
y_gm = tik_instance.Tensor("float16", (1024,), name="y_gm", scope=tik.scope_gm)
z_gm = tik_instance.Tensor("float16", (1024,), name="z_gm", scope=tik.scope_gm)

# On-chip Unified Buffer tensors
x_ub = tik_instance.Tensor("float16", (1024,), name="x_ub", scope=tik.scope_ubuf)
y_ub = tik_instance.Tensor("float16", (1024,), name="y_ub", scope=tik.scope_ubuf)
z_ub = tik_instance.Tensor("float16", (1024,), name="z_ub", scope=tik.scope_ubuf)

# GM -> UB
tik_instance.data_move(x_ub, x_gm, 0, 1, 64, 0, 0)
tik_instance.data_move(y_ub, y_gm, 0, 1, 64, 0, 0)

# Vector add over 1024 fp16 elements (mask=128 per repeat, 8 repeats)
tik_instance.vec_add(128, z_ub, x_ub, y_ub, 8, 1, 1, 1, 8, 8, 8)

# UB -> GM
tik_instance.data_move(z_gm, z_ub, 0, 1, 64, 0, 0)

tik_instance.BuildCCE(kernel_name="vec_add", inputs=[x_gm, y_gm], outputs=[z_gm])
```

## Tensor Declaration and Memory Scopes

`tik_instance.Tensor(dtype, shape, name, scope)` declares a tensor in a specific physical memory. The `scope` argument is the key control surface, mapping directly to the Ascend memory hierarchy:

| Scope constant   | Physical memory          | Typical use                                  |
|------------------|--------------------------|----------------------------------------------|
| `tik.scope_gm`   | Global Memory (HBM/DDR)  | Kernel inputs/outputs, host-visible buffers  |
| `tik.scope_ubuf` | Unified Buffer (UB)      | Working set for vector/reduce compute        |
| `tik.scope_cbuf` | L1 Buffer                | Staging for matrix/feature-map reuse         |

Vector and reduce instructions operate on `scope_ubuf` tensors only; data must first be staged into the UB. Declaring a tensor does not by itself emit a copy — movement is explicit via `data_move`. See `doc-ascend-memory-hierarchy` for the broader UB/L1/GM layout this scoping mirrors.

## Data Movement

`tik_instance.data_move(dst, src, sid, nburst, burst_len, src_stride, dst_stride)` is the MTE-backed transfer primitive used for GM↔UB (and UB↔L1) copies:

- `sid` — reserved channel/sync id, normally `0`.
- `nburst` — number of bursts (contiguous fragments) to transfer.
- `burst_len` — length of each burst in 32-byte units.
- `src_stride` / `dst_stride` — gap (in 32-byte units) between consecutive bursts, enabling strided/gather-style movement.

A single `data_move` with `nburst=1` and a `burst_len` covering the whole tensor performs a plain contiguous copy; larger `nburst` with non-zero strides expresses tiled or interleaved transfers without manual address arithmetic.

## Vector Compute APIs

Vector instructions execute on the Vector unit over UB-resident tensors. They share a common shape: an explicit `mask` (elements processed per repeat), a `repeat_times` count, and per-operand block/repeat strides that let one call sweep a large tensor.

```python
# Common signature pattern:
# vec_<op>(mask, dst, src0[, src1], repeat_times,
#          dst_blk_stride, src0_blk_stride[, src1_blk_stride],
#          dst_rep_stride, src0_rep_stride[, src1_rep_stride])

tik_instance.vec_add(128, dst_ub, a_ub, b_ub, 8, 1, 1, 1, 8, 8, 8)   # elementwise add
tik_instance.vec_sub(128, dst_ub, a_ub, b_ub, 8, 1, 1, 1, 8, 8, 8)   # elementwise subtract
tik_instance.vec_mul(128, dst_ub, a_ub, b_ub, 8, 1, 1, 1, 8, 8, 8)   # elementwise multiply
tik_instance.vec_max(128, dst_ub, a_ub, b_ub, 8, 1, 1, 1, 8, 8, 8)   # elementwise maximum
tik_instance.vec_exp(128, dst_ub, src_ub, 8, 1, 1, 8, 8)             # exp() (single source)
tik_instance.vec_rec(128, dst_ub, src_ub, 8, 1, 1, 8, 8)             # reciprocal (single source)
```

Common members:

- `vec_add` / `vec_sub` / `vec_mul` — binary arithmetic over two UB tensors.
- `vec_max` — elementwise maximum, the building block for stable softmax numerators.
- `vec_exp` / `vec_rec` — unary transcendental/reciprocal, used together for softmax and normalization (`vec_exp` then a reduce, then `vec_rec` of the denominator).

These primitives are the TIK-level equivalents of the higher-level Vector API described in `doc-ascendc-api-reference`; a softmax built from `vec_max` + `vec_exp` + reduce + `vec_rec` maps closely to the flow in `kernel-softmax-ascendc`.

## Reduction APIs

`vec_reduce_*` collapse a UB tensor along the element axis into a scalar (or per-repeat) result:

```python
tik_instance.vec_reduce_add(mask, dst_ub, src_ub, work_ub, repeat_times,
                            src_rep_stride)
tik_instance.vec_reduce_max(mask, dst_ub, src_ub, work_ub, repeat_times,
                            src_rep_stride)
```

- `vec_reduce_add` — sum reduction, e.g. the denominator of a softmax after `vec_exp`.
- `vec_reduce_max` — max reduction, e.g. the per-row maximum for numerically stable softmax.
- `vec_reduce_min` — min reduction.

A scratch UB tensor (`work_ub`) is passed for intermediate accumulation across repeats. As with the elementwise ops, all operands must reside in `scope_ubuf`.

## Loops and Double Buffering

`for_range` expands into a device-side loop. Passing `thread_num=2` enables ping-pong (double-buffered) execution: TIK automatically allocates two UB sub-buffers and overlaps `data_move` of the next tile with compute on the current tile, hiding MTE latency behind the Vector unit.

```python
loops = 8
tile = 128

with tik_instance.for_range(0, loops, thread_num=2) as i:
    x_ub = tik_instance.Tensor("float16", (tile,), name="x_ub", scope=tik.scope_ubuf)
    y_ub = tik_instance.Tensor("float16", (tile,), name="y_ub", scope=tik.scope_ubuf)
    z_ub = tik_instance.Tensor("float16", (tile,), name="z_ub", scope=tik.scope_ubuf)

    tik_instance.data_move(x_ub, x_gm[i * tile], 0, 1, tile // 16, 0, 0)
    tik_instance.data_move(y_ub, y_gm[i * tile], 0, 1, tile // 16, 0, 0)
    tik_instance.vec_add(tile, z_ub, x_ub, y_ub, 1, 1, 1, 1, 8, 8, 8)
    tik_instance.data_move(z_gm[i * tile], z_ub, 0, 1, tile // 16, 0, 0)
```

With `thread_num=1` the loop is single-buffered; `thread_num=2` is the standard double-buffering idiom and is the TIK realization of the technique described in `technique-double-buffering`. The reuse of the staged `x_ub`/`y_ub` across iterations is a form of `technique-data-reuse`.

## Compilation

`tik_instance.BuildCCE(kernel_name, inputs, outputs)` (also reachable via the lower-level `build` entry points) lowers the accumulated instruction stream through TBE/TVM into a `.o`/`.json` operator package for the target AI Core. The `inputs` and `outputs` lists bind `scope_gm` tensors to the kernel's external signature.

## Automatic vs. Manual Scheduling

A defining property of TIK is that the programmer specifies *what* to compute and *where* tensors live, while the compiler handles much of the *when*:

| Concern              | Who handles it in TIK                                              |
|----------------------|-------------------------------------------------------------------|
| UB address allocation| Automatic — TIK assigns offsets for declared `scope_ubuf` tensors  |
| Instruction ordering | Automatic — dependency graph inferred from tensor reads/writes     |
| Double buffering     | Semi-automatic — opt in via `for_range(..., thread_num=2)`         |
| Tiling / mask / strides | Manual — chosen by the developer per instruction               |
| Scope placement      | Manual — `scope_gm` / `scope_ubuf` / `scope_cbuf` chosen explicitly|

This contrasts with fully manual instruction scheduling: TIK frees the developer from hand-computing UB addresses and pipeline sync events, but still requires deliberate choices of tile size, mask, and stride to reach high utilization.

## Trade-offs and Pitfalls

- **Deprecated direction**: TIK is superseded by Ascend C for new development (see `doc-ascendc-api-reference`). It remains in use for legacy custom operators and cases where direct instruction-level control is preferred. New kernels should generally target Ascend C.
- **Mask vs. shape mismatch**: `mask` counts elements processed per repeat, not bytes; for fp16 a full vector is 128 elements. A `mask`/`repeat_times` product that under- or over-covers the tensor silently processes the wrong range.
- **Stride units are 32-byte blocks**: `burst_len` and the stride arguments in `data_move` are in 32-byte units, not elements — a frequent source of off-by-N transfer bugs.
- **Scope discipline**: vector and reduce instructions reject `scope_gm` operands; forgetting a `data_move` into `scope_ubuf` is a common error.
- **Double-buffer UB pressure**: `thread_num=2` doubles the live UB footprint of loop-body tensors; oversized tiles can exhaust the Unified Buffer.

## Notes

- TIK is built atop the TBE/TVM compilation stack; its tensors and loops lower to TVM IR before final code generation.
- Memory planning and dependency analysis are handled by TIK, but performance still hinges on developer-chosen tiling and double buffering.
- The Cube/matrix path on the AI Core is exercised through the broader TBE flow; for matrix-heavy kernels see `kernel-matmul-ascendc`, while TIK here focuses on the vector/MTE surface.

## Status

Verified against the official TIK API documentation. APIs (`Tensor`, `data_move`, `vec_add`/`vec_mul`/`vec_sub`/`vec_max`/`vec_exp`/`vec_rec`, `vec_reduce_add`/`vec_reduce_max`, `for_range`, `BuildCCE`) and scope constants (`scope_gm`, `scope_ubuf`, `scope_cbuf`) reflect the documented TIK surface. TIK is functional but deprecated in favor of Ascend C.
