---
id: kernel-add-tik
title: "TIK Vector Add — Elementwise Kernel in Python"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [elementwise, tbe-tik, tik, python]
confidence: source-reported
kernel_types: [elementwise]
languages: [tbe-tik, python]
sources: [doc-tik-api-reference, blog-tik-operator-walkthrough]
related: [lang-tik-guide, kernel-elementwise-ascendc, hw-vector-unit]
techniques: [double-buffering, data-reuse]
reproducibility: snippet
---

# TIK Vector Add — Elementwise Kernel in Python

## Overview

This page walks the full elementwise `z = x + y` operator written in TIK (Tensor Iterator Kernel), the low-level Python DSL inside TBE. It is the deliberate language-diversity counterpart to `kernel-elementwise-ascendc`: the same memory-bound, three-stage move-in / compute / move-out kernel, expressed as a host-side Python *builder* that emits an AI Core instruction stream rather than as a C++ kernel. The complete operator covers multi-core and in-core tiling, double-buffered `data_move`, the `vec_add` intrinsic, a masked tail, and the `BuildCCE` compile step. For the language reference behind these APIs see `lang-tik-guide`.

## Where TIK Add Sits

TIK is imperative Python that runs entirely on the host. `tik.Tik()` is a container; every `Tensor`, `data_move`, and `vec_add` call you make appends to an in-memory instruction stream that `BuildCCE` later lowers through the TBE/TVM stack into an AI Core binary. The Python loop body does not execute on device — `for_range` *expands* into a device-side loop. This is the same vector/MTE work that `kernel-elementwise-ascendc` performs on the Vector unit (`hw-vector-unit`); only the authoring surface differs.

The kernel is bandwidth-bound: it reads two fp16 operands and writes one, doing a single add per element, so the design goal is to keep the MTE pipeline saturated. The two levers TIK gives us for that are tiling (so each tile fits the Unified Buffer) and `thread_num=2` double buffering (so the move-in of the next tile overlaps the compute of the current one).

## Kernel Structure

The operator decomposes into four concerns:

1. **Multi-core tiling** — split the flat length across `block_num` AI Cores, one outer `for_range` over the block index.
2. **In-core tiling** — split each core's slice into UB-sized tiles, an inner `for_range(thread_num=2)` for double buffering.
3. **Per-tile pipeline** — `data_move` both operands GM→UB, `vec_add` on the UB tensors, `data_move` the result UB→GM.
4. **Tail handling** — a remainder tile shorter than the full tile, processed with a reduced `mask`.

## Full Operator

```python
from tbe import tik


def add_tik(length, kernel_name="add_tik"):
    tik_instance = tik.Tik()

    # --- tiling plan (host-side Python arithmetic) ---
    block_num = 8                     # AI Cores to split across
    dtype = "float16"
    block_elems = 16                  # 32-byte block holds 16 fp16
    vec_mask = 128                    # full fp16 vector width per repeat

    per_core = length // block_num    # elements handled by one core
    tile = 8 * 1024                   # UB tile size in elements (sized for 2x double buffer)
    loops = per_core // tile          # full tiles per core
    tail = per_core % tile            # leftover elements in the last partial tile

    # --- GM tensors: host-visible inputs x, y and output z ---
    x_gm = tik_instance.Tensor(dtype, (length,), name="x_gm", scope=tik.scope_gm)
    y_gm = tik_instance.Tensor(dtype, (length,), name="y_gm", scope=tik.scope_gm)
    z_gm = tik_instance.Tensor(dtype, (length,), name="z_gm", scope=tik.scope_gm)

    # --- outer loop: one iteration per AI Core ---
    with tik_instance.for_range(0, block_num, block_num=block_num) as core:
        core_off = core * per_core

        # --- inner loop: thread_num=2 => ping-pong UB double buffering ---
        with tik_instance.for_range(0, loops, thread_num=2) as i:
            off = core_off + i * tile

            x_ub = tik_instance.Tensor(dtype, (tile,), name="x_ub", scope=tik.scope_ubuf)
            y_ub = tik_instance.Tensor(dtype, (tile,), name="y_ub", scope=tik.scope_ubuf)

            # move in: GM -> UB (MTE). burst counted in 32-byte blocks => tile/16
            tik_instance.data_move(x_ub, x_gm[off], 0, 1, tile // block_elems, 0, 0)
            tik_instance.data_move(y_ub, y_gm[off], 0, 1, tile // block_elems, 0, 0)

            # compute: z = x + y on the Vector unit. repeat = tile/128, stride 8 blocks/repeat.
            # reuse x_ub as dst (data-reuse) so no third UB buffer is needed.
            tik_instance.vec_add(vec_mask, x_ub, x_ub, y_ub,
                                 tile // vec_mask, 1, 1, 1, 8, 8, 8)

            # move out: UB -> GM
            tik_instance.data_move(z_gm[off], x_ub, 0, 1, tile // block_elems, 0, 0)

        # --- tail: one shorter tile, masked vec_add over the remainder ---
        if tail:
            tail_off = core_off + loops * tile
            xt_ub = tik_instance.Tensor(dtype, (tile,), name="xt_ub", scope=tik.scope_ubuf)
            yt_ub = tik_instance.Tensor(dtype, (tile,), name="yt_ub", scope=tik.scope_ubuf)

            burst = (tail + block_elems - 1) // block_elems   # round up to whole blocks
            tik_instance.data_move(xt_ub, x_gm[tail_off], 0, 1, burst, 0, 0)
            tik_instance.data_move(yt_ub, y_gm[tail_off], 0, 1, burst, 0, 0)

            # mask = remaining elements (< 128) so the vector unit ignores the padding lanes
            tik_instance.vec_add(tail, xt_ub, xt_ub, yt_ub, 1, 1, 1, 1, 8, 8, 8)

            tik_instance.data_move(z_gm[tail_off], xt_ub, 0, 1, burst, 0, 0)

    # --- compile the accumulated instruction stream into a CCE kernel ---
    tik_instance.BuildCCE(kernel_name=kernel_name,
                          inputs=[x_gm, y_gm],
                          outputs=[z_gm])
    return tik_instance
```

### Reading the intrinsic arguments

- `data_move(dst, src, sid, nburst, burst, src_stride, dst_stride)` — `sid=0` is the reserved sync id, `nburst=1` is a single contiguous fragment, and `burst` is the fragment length **in 32-byte blocks** (hence `tile // 16` for fp16, not `tile`).
- `vec_add(mask, dst, src0, src1, repeat, dst_blk, src0_blk, src1_blk, dst_rep, src0_rep, src1_rep)` — `mask=128` processes one full fp16 vector per repeat, `repeat = tile // 128` sweeps the whole tile, block strides of `1` mean contiguous lanes, and repeat strides of `8` advance 8 blocks (one repeat) between iterations.
- In the tail, `mask` is set to the remaining element count (`< 128`) so the Vector unit operates only on valid lanes and leaves the block-padded remainder untouched.

## Tail and Mask Handling

The flat length rarely divides evenly into 128-lane vectors. The full-tile loop covers `loops * tile` elements per core; the remaining `tail` elements are processed in a single shorter tile. Two adjustments make the remainder correct:

- **`data_move` burst is rounded up** to whole 32-byte blocks (`(tail + 15) // 16`). MTE moves block-granular fragments, so the last block may carry a few padding elements past `tail`.
- **`vec_add` mask equals `tail`**, so the Vector unit computes exactly the valid lanes. The padding lanes inside the final block are read and (possibly) written but never contribute to a real output, because the matching `data_move` out writes only `tail` valid elements back to `z_gm`. This is the standard TIK idiom for a sub-vector remainder and mirrors the bounds clamp (`min(tile_size, total - offset)`) used in `kernel-elementwise-ascendc`.

## Double Buffering and Data Reuse

`for_range(0, loops, thread_num=2)` is the only thing required to enable double buffering: TIK allocates two physical UB sub-buffers for each loop-body tensor and overlaps the move-in of tile *t+1* with the compute of tile *t*, hiding MTE latency behind the Vector unit (`double-buffering`). Reusing `x_ub` as the `vec_add` destination instead of declaring a separate `z_ub` (`data-reuse`) frees UB budget — important because `thread_num=2` doubles the live footprint of every loop-body tensor.

## Comparison with the AscendC Version

Both implement the identical bandwidth-bound kernel; the difference is the authoring model. `kernel-elementwise-ascendc` uses C++ with `TPipe`/`TQue`, manual UB address management, and `DataCopy`/`Add` APIs; this TIK version is host-side Python where the framework plans UB addresses and instruction ordering for you.

| Aspect | TIK (this page) | AscendC (`kernel-elementwise-ascendc`) |
|---|---|---|
| Language | Python (imperative builder) | C/C++ kernel |
| Core loop body | ~6 calls per tile | ~3 high-level API calls per tile |
| UB addressing | Automatic (declare `scope_ubuf` Tensor) | Manual (`TPipe`/`TQue` allocation) |
| Instruction ordering | Automatic dependency graph | Manual + sync events |
| Double buffering | `thread_num=2` flag | Explicit queue depth |
| Mask / tile / stride | Manual (`mask`, `burst`, strides) | Manual (counts, bounds clamp) |
| Compile | `BuildCCE(...)` to a CCE `.o`/`.json` | Standard AscendC toolchain |
| Status | Legacy / deprecated | Recommended for new operators |

The TIK body is slightly longer per tile because it spells out three explicit `data_move` calls and the strided `vec_add` arguments, but it removes all manual queue/sync bookkeeping. AscendC reads denser at the call site yet exposes the pipeline events directly — more control and the modern path for new work.

## Trade-offs, Pitfalls, and Notes

- **Deprecated direction.** TIK is superseded by AscendC for new development; it persists mainly in legacy TBE custom operators. New elementwise kernels should follow `kernel-elementwise-ascendc`.
- **`thread_num=2` doubles UB pressure.** Double buffering allocates two copies of every loop-body UB tensor. Size `tile` for the doubled footprint, not the single-buffer one, or the Unified Buffer overflows.
- **`data_move` burst is in 32-byte blocks, not elements.** Passing `tile` where `tile // 16` (fp16) is required moves 16× too much data — a frequent off-by-N transfer bug.
- **`mask` is elements per repeat, not bytes.** fp16 processes 128 lanes per repeat; fp32 processes 64. Hard-coding `128` for an fp32 operator silently corrupts results; drive `mask` from `dtype`.
- **Tail burst must round up to whole blocks.** MTE moves block-granular fragments; rounding `tail` down truncates the final block and drops elements.
- **Scope discipline.** `vec_add` rejects `scope_gm` operands; forgetting a `data_move` into `scope_ubuf` is a common error.
- **Vector-only schedule.** This operator never touches the Cube unit — it is pure Vector-unit (`hw-vector-unit`) and MTE work. For matmul-shaped kernels use the Cube path in `kernel-matmul-ascendc` instead.

Per the `source-reported` confidence of this page, the API names and argument conventions above reflect the documented TIK surface (`doc-tik-api-reference`, `blog-tik-operator-walkthrough`); no benchmark figures are asserted here. The operator is bandwidth-bound, so realized throughput tracks HBM bandwidth and the effectiveness of the double-buffered move-in/compute overlap.
