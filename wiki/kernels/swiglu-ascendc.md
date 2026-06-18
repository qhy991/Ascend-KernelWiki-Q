---
id: kernel-swiglu-ascendc
title: "AscendC SwiGLU — Fused Gated Activation"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [swiglu, activation, elementwise, vector-unit, ascendc]
confidence: source-reported
kernel_types: [activation, elementwise]
languages: [ascendc]
sources: [doc-ascendc-api-reference, doc-ascend-operator-fusion, blog-ascendc-performance-tips]
related: [kernel-elementwise-ascendc, hw-vector-unit, technique-workspace-management]
techniques: [data-reuse, pipeline-scheduling]
reproducibility: snippet
---

# AscendC SwiGLU — Fused Gated Activation

SwiGLU is the gated activation at the heart of modern transformer FFN blocks (LLaMA, Qwen, and similar). It is defined as `SwiGLU(x) = Silu(gate) * up`, where `Silu(z) = z * sigmoid(z)`, and `gate` and `up` are the two halves of the FFN up-projection output. On Ascend NPU this maps cleanly onto the Vector unit, and — more importantly — the three logical operations (sigmoid, the silu multiply, and the gating multiply) can be **fused into a single kernel** so the activation reads the up-projection from Global Memory once and writes the result once.

## Why Fuse

The naïve route computes `Sigmoid`, then `Mul` for silu, then a second `Mul` for gating as three separate operators. Each unfused operator round-trips its tensors through Global Memory (GM), so a half-fused pipeline materializes intermediate tensors and pays roughly **3x the GM traffic** of the fused form. Since SwiGLU is bandwidth-bound, GM traffic is the cost that matters.

| Variant                          | GM reads        | GM writes | Intermediate GM tensors |
|----------------------------------|-----------------|-----------|-------------------------|
| Unfused (Sigmoid → Mul → Mul)    | gate + up + 2x  | 3x        | sigmoid, silu           |
| Fused single kernel (this page)  | gate + up       | 1x        | none (kept in UB)       |

The fused kernel keeps every intermediate (`sigmoid(gate)`, `silu = gate * sigmoid(gate)`) in the Unified Buffer (UB) and never spills it back to GM. This is a direct application of the workspace-reuse strategy described in technique-workspace-management, and it builds on the generic Vector template from kernel-elementwise-ascendc.

## Input Layout: Splitting gate and up

The FFN up-projection emits a single tensor of shape `[T, 2H]` where the first `H` columns are `gate` and the second `H` columns are `up` (the common interleaving for fused FFN-up GEMMs). The kernel slices each row into the two halves and processes them tile-by-tile:

```
row layout (one token, width 2H):
  [ g0 g1 ... g(H-1) | u0 u1 ... u(H-1) ]
    \---- gate ----/   \---- up -----/
```

`gate` and `up` for a tile are loaded into separate UB tensors with two `DataCopy` calls at the appropriate column offsets (a strided/offset copy), so no transpose or repacking is needed.

## Computing Silu on the Vector Unit

`Silu(z) = z * sigmoid(z)`. AscendC exposes `Sigmoid` directly on the Vector unit, so the silu reduces to one `Sigmoid` plus one `Mul`:

```ascendc
// silu(gate) = gate * sigmoid(gate), all in UB
Sigmoid(sig_ub, gate_ub, tile_len);   // sig_ub = sigmoid(gate)
Mul(silu_ub, gate_ub, sig_ub, tile_len);  // silu_ub = gate * sigmoid(gate)
```

When a hardware `Sigmoid` is unavailable or you want explicit control over the numerics, `sigmoid(z) = 1 / (1 + exp(-z))` can be built from `Exp`, `Adds`, and `Reciprocal`:

```ascendc
// sigmoid via Exp + reciprocal:  1 / (1 + exp(-z))
Muls(tmp_ub, gate_ub, -1.0f, tile_len);   // tmp = -gate
Exp(tmp_ub, tmp_ub, tile_len);            // tmp = exp(-gate)
Adds(tmp_ub, tmp_ub, 1.0f, tile_len);     // tmp = 1 + exp(-gate)
Reciprocal(sig_ub, tmp_ub, tile_len);     // sig = 1 / (1 + exp(-gate))
```

Both forms are numerically stable for the value ranges seen in FFN activations; the hardware `Sigmoid` path is preferred when available because it is a single Vector instruction.

## Complete Fused SwiGLU Kernel

```ascendc
extern "C" __global__ __aicore__ void swiglu_kernel(
    __gm__ uint8_t* GM_input,   // [T, 2H] : gate | up
    __gm__ uint8_t* GM_output,  // [T, H]
    int T, int H) {

    TPipe pipe;

    const int tile_len = 1024;             // elements per Vector tile
    const int stride2H  = 2 * H;           // row stride of the fused input

    // UB tensors: one tile each. silu reuses gate_ub in place (data reuse).
    auto gate_ub = AllocUB<half>(tile_len);
    auto up_ub   = AllocUB<half>(tile_len);
    auto sig_ub  = AllocUB<half>(tile_len);

    for (int t = 0; t < T; ++t) {
        int row_gate = t * stride2H;       // gate starts at column 0
        int row_up   = t * stride2H + H;   // up   starts at column H

        for (int off = 0; off < H; off += tile_len) {
            int len = min(tile_len, H - off);

            // --- CopyIn: gate and up halves into separate UB tensors ---
            DataCopy(gate_ub, GM_input + row_gate + off, len);
            DataCopy(up_ub,   GM_input + row_up   + off, len);

            // --- Compute silu(gate) = gate * sigmoid(gate) ---
            Sigmoid(sig_ub, gate_ub, len);          // sig = sigmoid(gate)
            Mul(gate_ub, gate_ub, sig_ub, len);     // gate_ub <- silu (in place)

            // --- Gate: SwiGLU = silu(gate) * up ---
            Mul(gate_ub, gate_ub, up_ub, len);      // gate_ub <- silu * up

            // --- Single CopyOut: one write per output element ---
            DataCopy(GM_output + t * H + off, gate_ub, len);
        }
    }
}
```

The output `gate_ub` is reused in place across both `Mul` calls, so the kernel needs only three UB tensors per tile, and there is exactly **one** `DataCopy` write per output element.

## UB Reuse and Buffer Budget

The in-place chaining (`silu` overwriting `gate_ub`, then the gating multiply overwriting it again) keeps the live UB footprint at three tiles regardless of `H`. This matters because a larger tile budget lets the scheduler overlap the next tile's `CopyIn` with the current tile's Vector work — the same pipeline-scheduling pattern used by kernel-elementwise-ascendc. With a strict three-tensor budget you can afford double-buffering of `gate_ub`/`up_ub` for that overlap:

```ascendc
// double-buffered CopyIn for tile (n+1) while computing tile (n)
pipe.CopyIn(gate_ub_next, GM_input + row_gate + next_off, len);
pipe.CopyIn(up_ub_next,   GM_input + row_up   + next_off, len);
Sigmoid(sig_ub, gate_ub_cur, len);
Mul(gate_ub_cur, gate_ub_cur, sig_ub, len);
Mul(gate_ub_cur, gate_ub_cur, up_ub_cur, len);
pipe.CopyOut(GM_output + out_off, gate_ub_cur, len);
```

## Vector Unit API Reference

Key AscendC Vector APIs used by this kernel:

- **DataCopy**: `DataCopy(dst, src, count)` — GM↔UB transfer (used here with column offsets to slice gate/up)
- **Sigmoid**: `Sigmoid(LocalTensor& dst, LocalTensor& src, int count)` — elementwise logistic sigmoid
- **Mul**: `Mul(LocalTensor& dst, LocalTensor& src1, LocalTensor& src2, int count)` — elementwise multiply (used for both silu and gating)
- **Exp**: `Exp(LocalTensor& dst, LocalTensor& src, int count)` — elementwise exponentiation (sigmoid fallback)
- **Reciprocal**: `Reciprocal(LocalTensor& dst, LocalTensor& src, int count)` — elementwise reciprocal (sigmoid fallback)
- **Adds / Muls**: `Adds(dst, src, scalar, count)` / `Muls(dst, src, scalar, count)` — scalar add / multiply

## Trade-offs, Pitfalls, and Notes

- **Fusion vs. reuse of stock operators.** The unfused `Sigmoid → Mul → Mul` chain is trivial to assemble from library operators but pays ~3x GM traffic. Fusing trades that bandwidth for a small amount of custom-kernel maintenance; for a bandwidth-bound op this is almost always the right call. See doc-ascend-operator-fusion for the general fusion rationale.
- **Layout assumption.** The kernel assumes the `gate | up` concatenation along the last dimension `[T, 2H]`. If the FFN-up GEMM emits gate and up as two separate tensors, drop the column-offset slicing and issue two plain `DataCopy` loads instead — the compute path is unchanged.
- **dtype and numerics.** FFN activations are typically fp16. The hardware `Sigmoid` path keeps everything in one Vector instruction; the `Exp + Reciprocal` fallback introduces an extra rounding step but stays within the safe range of FFN gate magnitudes. Accumulating the gate in fp32 is unnecessary here because there is no reduction.
- **Silu is not a separate Silu API.** This kernel composes `Sigmoid` + `Mul` rather than calling a monolithic silu, which keeps the intermediate `sigmoid(gate)` available and makes the in-place UB reuse explicit. The generic elementwise template (kernel-elementwise-ascendc) lists `Silu` as `Mul(out, in, Sigmoid(in))` for the same reason.
- **Tile size.** `tile_len` should divide the UB budget so that gate, up, and the sigmoid scratch all fit alongside a double-buffer copy; 1024 fp16 elements per tensor is a reasonable starting point on Ascend 910B.

## Relation to Other Pages

SwiGLU sits downstream of the FFN up-projection GEMM (see kernel-matmul-ascendc) and reuses the Vector-unit machinery documented in hw-vector-unit and the elementwise template in kernel-elementwise-ascendc. The single-CopyOut, no-intermediate-spill design is the activation-specific instance of the workspace strategy in technique-workspace-management. As a confidence-`source-reported` page, the 3x GM-traffic reduction is the grounded, sourced claim; no absolute throughput numbers are asserted for this kernel.
