---
id: blog-tik-operator-walkthrough
title: "TIK Operator Walkthrough — Writing Vector Add and Softmax in Python"
type: source-blog
author: cann-community
date: '2025-08-15'
url: https://support.huaweicloud.com/intl/en-us/odevg-A800_3000_3010/atlaste_07_0082.html
architectures: [ascend910, ascend910b]
tags: [tbe-tik, tik, python, operator, tutorial]
techniques: [double-buffering, data-reuse]
hardware_features: [unified-buffer, vector-unit, mte]
kernel_types: [elementwise, softmax]
languages: [tbe-tik, python]
confidence: source-reported
---

TIK (Tensor Iterator Kernel) is the low-level Python DSL in TBE for hand-writing Ascend operators when the higher-level DSL cannot express the schedule you want. This walkthrough builds two operators end to end — an elementwise vector add and a row-wise softmax — covering `tik_instance` setup, GM/UB tensor allocation, a double-buffered `data_move` tiling loop, the vector intrinsics, and how `BuildCCE` produces an object you can wrap in a custom op plugin. It pairs naturally with the AscendC-based implementations in `kernel-elementwise-ascendc` and `kernel-softmax-ascendc`, and with `migration-tbe-to-ascendc` if you later port these forward.

## Why TIK

TIK gives you explicit control over the memory hierarchy and the vector pipeline. You decide what lives in Global Memory (GM) versus Unified Buffer (UB), how data is tiled, and which vector intrinsics run on the Vector unit. Compared to TBE-DSL (see `lang-tbe-dsl-guide`), TIK trades automatic scheduling for the ability to hand-tune tiling and double buffering — useful when an operator is bound by MTE transfers rather than compute.

The mental model is a three-stage loop per tile: **move in** (GM → UB via MTE), **compute** (Vector unit intrinsics on UB tensors), **move out** (UB → GM). Double buffering overlaps the move-in of tile *t+1* with the compute of tile *t*.

## Vector Add

The add operator is the canonical "hello world" for TIK. We tile the flat input across `data_move` iterations and use `for_range(thread_num=2)` so the framework allocates ping-pong UB buffers automatically.

```python
from tbe import tik

def vector_add(kernel_name="vector_add"):
    tik_instance = tik.Tik()

    total = 1024 * 1024          # elements
    tile = 8 * 1024              # elements per tile (fits UB with 2x double buffer)
    loops = total // tile

    # GM tensors: inputs x, y and output z
    x_gm = tik_instance.Tensor("float16", (total,), name="x_gm", scope=tik.scope_gm)
    y_gm = tik_instance.Tensor("float16", (total,), name="y_gm", scope=tik.scope_gm)
    z_gm = tik_instance.Tensor("float16", (total,), name="z_gm", scope=tik.scope_gm)

    # thread_num=2 => TIK manages ping-pong UB buffers for double buffering
    with tik_instance.for_range(0, loops, thread_num=2) as i:
        x_ub = tik_instance.Tensor("float16", (tile,), name="x_ub", scope=tik.scope_ubuf)
        y_ub = tik_instance.Tensor("float16", (tile,), name="y_ub", scope=tik.scope_ubuf)

        # move in: GM -> UB (MTE). burst counts a fp16 block = 16 elements => tile/16
        tik_instance.data_move(x_ub, x_gm[i * tile], 0, 1, tile // 16, 0, 0)
        tik_instance.data_move(y_ub, y_gm[i * tile], 0, 1, tile // 16, 0, 0)

        # compute: z = x + y on the Vector unit. repeat=tile/128 (128 fp16 / repeat)
        tik_instance.vec_add(128, x_ub, x_ub, y_ub, tile // 128, 1, 1, 1, 8, 8, 8)

        # move out: UB -> GM
        tik_instance.data_move(z_gm[i * tile], x_ub, 0, 1, tile // 16, 0, 0)

    tik_instance.BuildCCE(kernel_name=kernel_name,
                          inputs=[x_gm, y_gm],
                          outputs=[z_gm])
    return tik_instance
```

A few notes on the intrinsic arguments:

- `vec_add(mask, dst, src0, src1, repeat, dst_blk, src0_blk, src1_blk, dst_rep, src0_rep, src1_rep)` — `mask=128` processes 128 fp16 lanes per repeat (one full vector instruction width). The block strides of `1` read consecutive 32-byte blocks within a repeat; the repeat strides of `8` advance one full 256-byte vector (8 blocks) per repeat, i.e. contiguous data.
- `data_move(dst, src, sid, nburst, burst, src_gap, dst_gap)` — `burst` is counted in 32-byte blocks, so `tile // 16` for fp16.
- Reusing `x_ub` as the destination avoids a third UB buffer (`data-reuse`), leaving more UB budget for the double-buffered ping-pong.

## Softmax

Row-wise softmax is the same move-in / compute / move-out skeleton, but the compute stage is a five-intrinsic numerically-stable sequence. For each row we subtract the row max before exponentiating to avoid `exp` overflow.

The pattern is:

1. `vec_reduce_max` — reduce each row to its max.
2. `vec_sub` — broadcast-subtract the per-row max from every element.
3. `vec_exp` — elementwise exponential.
4. `vec_reduce_add` — reduce each row to its sum.
5. `vec_rec` — reciprocal of the row sum.
6. `vec_mul` — multiply exponentials by the reciprocal to normalize.

```python
from tbe import tik

def softmax(rows, cols, kernel_name="softmax"):
    tik_instance = tik.Tik()
    shape = (rows, cols)

    x_gm = tik_instance.Tensor("float16", shape, name="x_gm", scope=tik.scope_gm)
    y_gm = tik_instance.Tensor("float16", shape, name="y_gm", scope=tik.scope_gm)

    with tik_instance.for_range(0, rows, thread_num=2) as r:
        x_ub  = tik_instance.Tensor("float16", (cols,), name="x_ub",  scope=tik.scope_ubuf)
        wk    = tik_instance.Tensor("float16", (cols,), name="wk",    scope=tik.scope_ubuf)
        mx    = tik_instance.Tensor("float16", (16,),   name="mx",    scope=tik.scope_ubuf)
        sm    = tik_instance.Tensor("float16", (16,),   name="sm",    scope=tik.scope_ubuf)

        # move one row in
        tik_instance.data_move(x_ub, x_gm[r, 0], 0, 1, cols // 16, 0, 0)

        # 1) row max   (wk = a SEPARATE work_tensor scratch; must not alias the source)
        tik_instance.vec_reduce_max(cols, mx, x_ub, wk, 1, 1)
        # 2) subtract broadcast max: x = x - max   (src1 scalar broadcast over the row)
        tik_instance.vec_sub(cols, x_ub, x_ub, mx, 1, 8, 8, 0)
        # 3) exponentiate
        tik_instance.vec_exp(cols, x_ub, x_ub, 1, 8, 8)
        # 4) row sum   (reuse the wk scratch, still distinct from the x_ub source)
        tik_instance.vec_reduce_add(cols, sm, x_ub, wk, 1, 1)
        # 5) reciprocal of the sum
        tik_instance.vec_rec(16, sm, sm, 1, 1, 1)
        # 6) normalize: x = x * (1/sum)
        tik_instance.vec_mul(cols, x_ub, x_ub, sm, 1, 8, 8, 0)

        # move the normalized row out
        tik_instance.data_move(y_gm[r, 0], x_ub, 0, 1, cols // 16, 0, 0)

    tik_instance.BuildCCE(kernel_name=kernel_name,
                          inputs=[x_gm],
                          outputs=[y_gm])
    return tik_instance
```

The `vec_sub` and `vec_mul` calls pass a `src1_stride` of `0` so the single per-row scalar in `mx` / `sm` is broadcast across the whole row rather than advancing. This is the TIK idiom for "operate a vector against a scalar". The AscendC equivalent of this whole sequence is documented in `kernel-softmax-ascendc`; the numerically-stable max-subtraction is the same idea used in the online-softmax variant of flash attention.

## From BuildCCE to a Custom Op Plugin

`tik_instance.BuildCCE(kernel_name, inputs, outputs)` compiles the schedule into a CCE kernel binary plus a `.json` description of the kernel name, block dimension, and tensor signatures. To make the operator callable from a framework graph you wrap it in a custom op plugin:

| Artifact | Produced by | Role |
|---|---|---|
| `<kernel_name>.o` / `.json` | `BuildCCE` | Compiled kernel + launch metadata |
| Op proto (`.h`/registration) | hand-written | Declares inputs/outputs/attrs to the graph |
| Op info `.ini` | hand-written | Shape/dtype constraints for op selection |
| TF/Torch adapter | hand-written | Maps framework node to the TIK op |

The plugin registers the op so the graph engine can match a node, select the TIK implementation, and dispatch the compiled kernel at runtime. The `kernel_name` you pass to `BuildCCE` must match the name referenced by the op info file.

## Trade-offs, Pitfalls, and Notes

- **`thread_num=2` doubles UB pressure.** Double buffering allocates two copies of every UB tensor inside the `for_range`. If a tile already nearly fills `unified-buffer` (`hw-unified-buffer`), enabling ping-pong can overflow it. Size `tile` for the doubled footprint, not the single-buffer one.
- **`mask` / element-width mismatch.** fp16 intrinsics process 128 lanes per repeat; fp32 process 64. Hard-coding `128` for an fp32 operator silently corrupts results. Drive `mask` and `repeat` from `dtype`.
- **`data_move` burst is in 32-byte blocks, not elements.** A common bug is passing `tile` (elements) where `tile // 16` (fp16 blocks) is required, moving 16x too much data.
- **Broadcast needs `src1_stride = 0`.** Forgetting this in `vec_sub`/`vec_mul` reads past the 16-element scalar buffer and subtracts garbage.
- **Reduce intrinsics write a small vector, not a scalar.** `vec_reduce_max` / `vec_reduce_add` emit a per-block result; keep the destination buffer (`mx`, `sm`) at least one block (16 fp16) wide.
- **Reduce needs a separate `work_tensor`.** The 4th argument to `vec_reduce_max`/`vec_reduce_add` is a scratch `work_tensor` (here `wk`) for cross-repeat accumulation; it must be **distinct from the source** tensor. Aliasing the source (passing `x_ub` as both src and work) corrupts the row mid-reduction. Size it per the API guidance (roughly the source width for fp16).
- **Vector-only schedule.** These operators never touch the Cube unit — they are pure Vector-unit (`hw-vector-unit`) and MTE work. For matmul-shaped kernels use the Cube path described in `kernel-matmul-ascendc` instead.

### When to reach for TIK vs DSL

| Aspect | TBE-DSL | TIK |
|---|---|---|
| Scheduling | automatic | manual (`for_range`, explicit `data_move`) |
| Double buffering | inferred | explicit `thread_num=2` |
| Best for | standard fused elementwise | custom tiling, irregular access, hand-tuned pipelines |
| Effort | low | higher |

For new work the recommended path is AscendC rather than TIK; `migration-tbe-to-ascendc` covers moving an existing TIK operator forward while preserving the same move-in / compute / move-out structure shown here.
