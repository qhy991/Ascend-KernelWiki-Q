---
id: wiki-hardware-l1-l0-buffer
title: "L1 and L0 Buffers — The Cube Unit's On-Chip Staging Hierarchy"
type: wiki-hardware
architectures: [ascend910, ascend910b]
tags: [l1-buffer, l0-buffer, memory, cube-unit, hardware]
confidence: source-reported
hardware_features: [l1-buffer, l0-buffer, unified-buffer, cube-unit]
cuda_equivalent: l1_cache
related: [wiki-hardware-memory-hierarchy, wiki-hardware-cube-unit, wiki-hardware-unified-buffer]
sources: [doc-ascend-memory-hierarchy, doc-catlass-framework, blog-ascend-910b-deep-dive]
---

# L1 and L0 Buffers — The Cube Unit's On-Chip Staging Hierarchy

The L1 buffer and the L0A/L0B/L0C buffers form the dedicated staging path that feeds the Cube unit (hw-cube-unit). They sit between Global Memory and the Cube MAC array, holding matrix tiles close enough to the compute engine to sustain its throughput. This page describes the matmul dataflow through this hierarchy and how it constrains tiling.

## Staging Path Overview

For a matmul `C = A × B`, operands flow through a strict on-chip pipeline before and after the Cube MAC array. Each level trades capacity for proximity to the compute units:

```
┌────────────────────────────────────────────────────────────┐
│ Global Memory (GM / HBM)                                    │
│ A, B operands and C output in main memory                   │
└────────────────────────────────────────────────────────────┘
                  │  DataCopy (via MTE)
                  ▼
┌────────────────────────────────────────────────────────────┐
│ L1 Buffer  (~1 MB)                                          │
│ Large on-chip SRAM. Holds tiles of A and B for reuse.       │
│ Ping-pong (double-buffered) to overlap load with compute.   │
└────────────────────────────────────────────────────────────┘
          │ left tile               │ right tile
          ▼                         ▼
┌──────────────────────┐  ┌──────────────────────┐
│ L0A (tens of KB)     │  │ L0B (tens of KB)     │
│ Left matrix (A)      │  │ Right matrix (B)     │
│ fragments            │  │ fragments            │
└──────────────────────┘  └──────────────────────┘
          │                         │
          └───────────┬─────────────┘
                      ▼
        ┌───────────────────────────────┐
        │ Cube MAC array (hw-cube-unit) │
        │ Multiply-accumulate           │
        └───────────────────────────────┘
                      │
                      ▼
┌────────────────────────────────────────────────────────────┐
│ L0C  (tens of KB)                                           │
│ Accumulator buffer. Partial sums held in FP32.              │
└────────────────────────────────────────────────────────────┘
                  │  DataCopy
                  ▼
┌────────────────────────────────────────────────────────────┐
│ Unified Buffer (UB) → Global Memory (GM)                    │
│ Optional vector epilogue, then write back                   │
└────────────────────────────────────────────────────────────┘
```

The path is therefore: **GM → L1 → L0A/L0B → Cube → L0C (FP32 accumulate) → UB/GM**.

## Level-by-Level Breakdown

### L1 Buffer
- **Role**: Large on-chip SRAM that stages tiles of both `A` and `B` after they are copied in from GM.
- **Capacity**: ~1 MB per AICore (source-reported; varies by chip generation).
- **Why it matters**: A single L1-resident tile of `A` or `B` can feed many Cube MAC passes, so the cost of the GM→L1 transfer is amortized over substantial reuse. This is the primary place where matmul data reuse is realized.
- **Management**: Explicit. Tiles are loaded with `DataCopy` and the buffer is partitioned by the kernel author or by the Catlass framework (doc-catlass-framework).

### L0A and L0B Buffers
- **Role**: Feed the Cube MAC array directly. **L0A** holds fragments of the *left* matrix (`A`); **L0B** holds fragments of the *right* matrix (`B`).
- **Capacity**: Tens of KB each — much smaller than L1.
- **Why they matter**: They hold exactly the operand fragments the MAC array consumes on the current pass. Because they are small, the L1 tile is streamed into L0A/L0B in sub-tiles, and tiling must keep each sub-tile within L0 capacity.

### L0C Buffer
- **Role**: The Cube accumulator. Partial sums from successive K-steps accumulate here.
- **Precision**: **FP32**, even when inputs are FP16/BF16. This preserves accumulation accuracy across the K dimension before the result is cast down or written out.
- **Capacity**: Tens of KB.
- **Drain path**: Results are copied from L0C to UB (hw-unified-buffer) — where an optional vector epilogue such as bias-add or activation runs on the Vector unit — and then to GM, or copied out directly.

## Why the Hierarchy Enables Reuse and Ping-Pong

Two ideas drive the design:

1. **Data reuse.** A GM access costs ~100+ cycles (see wiki-hardware-memory-hierarchy). By staging a tile of `A` in L1 once and reusing it against many tiles of `B` (and vice versa), the expensive GM traffic is amortized over a large number of MAC operations. The L0 buffers then deliver operand fragments at near-MAC-array bandwidth.

2. **Ping-pong (double buffering).** Because L1 and L0 are explicitly managed, the kernel can hold *two* tiles per level: while the Cube array consumes one buffer, the MTE engine loads the next. The Catlass framework exposes this as the **`MmadAtlasA2Pingpong`** policy, which double-buffers the L1/L0 staging so that GM→L1 and L1→L0 transfers overlap with Cube compute. This is the matmul-specific instance of the double-buffering technique (technique-double-buffering) on the Cube path.

```cpp
// Catlass GEMM with ping-pong (double-buffered) L1/L0 staging.
// MmadAtlasA2Pingpong overlaps GM->L1 / L1->L0 loads with Cube MACs.
using BlockMmad = Catlass::Gemm::Block::BlockMmad<
    MmadAtlasA2Pingpong,   // double-buffer L1/L0 to hide load latency
    L1TileShape,           // tile of A,B staged in L1 (must fit ~1 MB)
    L0TileShape>;          // sub-tile streamed into L0A/L0B (tens of KB)
```

The L1 and L0 tile shapes are not free parameters: each must respect the capacity of its level, which is what makes tiling a hardware-constrained problem (technique-tiling-strategy).

## Tiling Must Respect L1/L0 Sizes

The matmul tiling strategy (technique-tiling-strategy) is bounded at two levels simultaneously:

- The **L1 tile** of `A` plus the L1 tile of `B` (times two if ping-pong is enabled) must fit within ~1 MB.
- The **L0 sub-tile** streamed from L1 into L0A/L0B must fit within the tens-of-KB L0 capacity, and the corresponding output block must fit in L0C as FP32.

If a tile is chosen too large, it overflows the buffer and the schedule is invalid; too small, and the GM→L1 transfer is under-amortized and reuse drops. A kernel such as kernel-matmul-ascendc selects L1/L0 tile shapes so both constraints hold while maximizing reuse — exactly the balance the Catlass tiling policies automate.

| Buffer | Capacity (approx) | Holds | Precision | Feeds |
|--------|-------------------|-------|-----------|-------|
| L1 | ~1 MB | Tiles of A and B | input dtype | L0A / L0B |
| L0A | tens of KB | Left (A) fragments | input dtype | Cube MAC array |
| L0B | tens of KB | Right (B) fragments | input dtype | Cube MAC array |
| L0C | tens of KB | Accumulated partial sums | FP32 | UB / GM |

## Contrast with the Unified Buffer (Vector Path)

The L1/L0 chain is the **Cube** unit's staging path. The Unified Buffer (hw-unified-buffer) is the **Vector** unit's scratchpad. They are distinct on-chip memories serving distinct compute engines:

| Aspect | L1 + L0A/L0B/L0C | Unified Buffer (UB) |
|--------|------------------|---------------------|
| Feeds | Cube MAC array | Vector unit |
| Operands | Matrix tiles / fragments | Elementwise vectors |
| L0C precision | FP32 accumulator | n/a |
| Role in matmul | Stage A/B, accumulate C | Epilogue + write-back staging |
| Programming model | L1/L0 tile shapes, ping-pong | `TPipe` / `TBuf`, DataCopy |

In a fused matmul, both paths cooperate: the Cube produces C in L0C, the result lands in UB, and any vector epilogue (bias, GELU, scaling) runs there before the write to GM.

## Pitfalls and Notes

1. **L0 is not L1.** Sizing a tile for L1 (~1 MB) but forgetting the much smaller L0A/L0B/L0C (tens of KB) is the most common tiling error. Both constraints must hold.
2. **FP32 accumulation cost.** L0C holds FP32 partial sums, so the output footprint per tile is larger than the FP16/BF16 inputs suggest — budget L0C accordingly.
3. **Ping-pong doubles the footprint.** `MmadAtlasA2Pingpong` keeps two tiles live per level; the L1 budget must accommodate two A/B tiles, not one.
4. **Reuse, not just residency.** Putting a tile in L1 only pays off if it is reused many times. Tiles that are touched once gain little from the staging hierarchy.
5. **Confidence.** Capacities here (L1 ~1 MB; L0A/L0B/L0C tens of KB) are source-reported and generation-dependent; treat them as design-guidance magnitudes rather than exact device constants.

## Best Practices

1. **Size L1 tiles for reuse**: choose the largest A/B tiles that fit ~1 MB (and fit twice when ping-pong is on) to amortize GM traffic.
2. **Sub-tile for L0**: stream L1 tiles into L0A/L0B in fragments that fit the tens-of-KB L0 buffers.
3. **Enable ping-pong**: use `MmadAtlasA2Pingpong` (doc-catlass-framework) to overlap load and compute on the Cube path.
4. **Keep accumulation in L0C**: let FP32 partial sums accumulate across the K dimension before draining to UB/GM.
5. **Separate the two paths**: do not conflate L1/L0 (Cube) sizing with UB (Vector) sizing — they are independent budgets (hw-memory-hierarchy).
