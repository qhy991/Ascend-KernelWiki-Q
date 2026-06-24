---
id: pattern-tiling-too-small
title: "Tiling Too Small — Under-Utilized Cube and MTE"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [tiling, cube-unit, diagnosis, performance, pattern]
confidence: source-reported
symptoms: ["Cube utilization low despite a compute-bound shape", "many short MTE transfers", "tile dims below the 16x16 fractal", "kernel time dominated by loop and sync overhead"]
techniques: [tiling-strategy, nz-tiling]
related: [pattern-low-cube-utilization, technique-tiling-strategy, wiki-hardware-cube-unit]
sources: [doc-ascendc-tiling-api, doc-catlass-framework, doc-ascend-profiling-guide]
---

Tiles that are chosen too small are the mirror image of the memory-bound failure in pattern-memory-bound: instead of spilling out of the Unified Buffer (UB), the kernel never gives the Cube MAC array or the MTE burst engines enough work per iteration. The result is a compute-bound matmul that *should* saturate the Cube but instead leaves it idle while loop counters, address calculation, and synchronization dominate the timeline. This page covers how to recognize the pattern and how to grow tiles back toward the hardware sweet spot without crossing into the spilling regime.

## Problem

The Cube unit on Ascend consumes data in the 16×16 FRACTAL_NZ fractal: every matmul issue operates on a `16×16×16` MAC block. When `tile_M`, `tile_N`, or `tile_K` are picked below the size that fills the L0A/L0B/L0C buffers — or worse, below a single fractal — each Cube instruction does very little real work, yet still pays the full fixed cost of an instruction issue, an address update, and a pipeline dependency check.

The same logic applies to the MTE: `DataCopy` is most efficient when it moves long, contiguous bursts from Global Memory (GM) into L1 / UB. Tiny tiles turn one large efficient transfer into many short bursts, so MTE startup latency is never amortized.

Because the arithmetic intensity of the *shape* is high (it is genuinely compute-bound), profilers do not flag a bandwidth problem. Instead the wall-clock time is eaten by loop overhead and `PipeBarrier`/event synchronization between hundreds of tiny iterations — the kernel is *overhead-bound*, a sub-case of the broader pattern-low-cube-utilization.

## Diagnostic Symptoms (via msprof / the profiling guide)

Following doc-ascend-profiling-guide, this pattern shows a distinctive signature:

- **Low Cube utilization on a compute-bound shape** — the FLOP/byte ratio of the problem is high, yet `cube_fops` utilization sits well below the memory-bound threshold you would expect for the shape.
- **Many tiny MTE bursts** — the DataCopy timeline shows a large count of short transfers rather than a few long ones; per-transfer setup latency dominates MTE busy time.
- **Tile dims below the 16×16 fractal, or not a multiple of 16** — `tile_M % 16 != 0` (or N, K) forces padding inside each fractal, so part of every MAC block is wasted.
- **Kernel time dominated by loop + sync overhead** — `PipeBarrier`, event waits, and the scalar loop body take a disproportionate share of the timeline relative to actual `Matmul` issue time.

```
Shape is compute-bound (high FLOP/byte)?
├─ No  → see pattern-memory-bound instead
└─ Yes → Check Cube utilization in msprof
    ├─ High (>~70%) → already healthy, stop
    └─ Low → Check MTE transfer profile
        ├─ Few long bursts → look at sync/barriers (pattern-pipeline-stall)
        └─ Many short bursts → TILING TOO SMALL
            ├─ tile dims < 16 or not %16 → align to fractal first
            └─ tiles fit L0/L1 with room to spare → grow tile_M/N/K
```

## Root Causes

### 1. Tile dimensions below the Cube fractal
A `tile_M`/`tile_N`/`tile_K` smaller than 16 cannot fill a single `16×16` MAC block, so the Cube pads and discards. Even at exactly 16, a single fractal per issue means the loop body runs thousands of times for a large GEMM, and instruction-issue overhead dominates.

### 2. Tiles that under-fill L0/L1
The Cube reads its operands from L0A/L0B and accumulates in L0C; L1 stages the data copied from GM. If the chosen tile only occupies a small fraction of these buffers, the kernel issues far more outer-loop iterations than necessary, and the MTE moves the same total bytes in many short bursts.

### 3. Misalignment forcing padding
Dimensions that are not multiples of 16 (e.g. `K=129`) force the host tiling to round up, wasting a partial fractal on every iteration — small tiles make this proportionally worse because the wasted fraction is large relative to the useful work.

## Solutions

### Grow tile_M / tile_N / tile_K to fill the on-chip buffers
The primary fix is to make each iteration do more real work. Increase the tile dimensions until the L0/L1 operand footprint is well-filled, while leaving headroom for double buffering — recall from pattern-pipeline-stall that two tiles (current + next) plus the output accumulator must coexist in UB/L1 for the MTE/Cube overlap to work. Grow toward the buffers, then stop one step before you would spill into pattern-memory-bound.

### Align every tile dimension to the 16×16 fractal
Always make `tile_M`, `tile_N`, and `tile_K` multiples of 16 so each Cube issue maps cleanly onto whole fractals with no padding. This is the same alignment requirement enforced for FRACTAL_NZ data in pattern-nz-format-traps.

### Let the host tiling pick shape-appropriate tiles
Rather than hard-coding tile sizes, use the AscendC host-side Tiling API (doc-ascendc-tiling-api) to compute tiles from the actual `M, N, K` and the available L0/L1/UB budget. This is the core of technique-tiling-strategy: the host computes a `TCubeTiling` (or equivalent) that the kernel reads through `GET_TILING_DATA`, so the same kernel adapts to large and small shapes without recompilation. Frameworks such as Catlass (doc-catlass-framework) wrap this selection so the tile shape tracks the problem shape automatically.

```cpp
// Host side: derive tiles from the real shape and buffer budget,
// instead of a fixed (too-small) tile. AscendC Tiling API.
#include "tiling/platform/platform_ascendc.h"
#include "tiling/tiling_api.h"

using namespace matmul_tiling;

void GenerateMatmulTiling(uint32_t M, uint32_t N, uint32_t K,
                          optiling::TCubeTiling &cubeTiling) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(/* context */);
    MatmulApiTiling mmTiling(ascendcPlatform);

    mmTiling.SetAType(TPosition::GM, CubeFormat::ND, DataType::DT_FLOAT16);
    mmTiling.SetBType(TPosition::GM, CubeFormat::ND, DataType::DT_FLOAT16);
    mmTiling.SetCType(TPosition::GM, CubeFormat::ND, DataType::DT_FLOAT);

    mmTiling.SetShape(M, N, K);
    mmTiling.SetOrgShape(M, N, K);

    // Let the API fill L0/L1 rather than forcing a tiny tile.
    // SetFixSplit can constrain singleCoreM/N/K to fractal-aligned values.
    mmTiling.SetFixSplit(-1, -1, -1);   // -1 => API chooses to fill buffers
    mmTiling.SetBufferSpace(-1, -1, -1); // -1 => use full L1/L0C budget

    if (mmTiling.GetTiling(cubeTiling) == -1) {
        // fall back / report: requested split could not be satisfied
    }
}
```

```cpp
// Kernel side: read the host-computed tiling instead of literals.
extern "C" __global__ __aicore__ void matmul_kernel(GM_ADDR a, GM_ADDR b,
                                                    GM_ADDR c, GM_ADDR workspace,
                                                    GM_ADDR tilingGm) {
    GET_TILING_DATA(tiling, tilingGm);  // pulls the TCubeTiling chosen on host
    // tiling.singleCoreM / singleCoreN / singleCoreK are fractal-aligned
    // and sized to fill L0/L1 — not the original too-small literals.
    // ... configure Matmul<> with tiling and run ...
}
```

### Balance against the opposite failure mode
Growing tiles is bounded on the other side by spilling. If you push `tile_M × tile_N × tile_K` past what L1/UB can hold (remembering the ~1.06× NZ expansion noted in pattern-nz-format-traps and the double-buffer footprint), the kernel falls into pattern-memory-bound: extra GM round-trips reappear and bandwidth becomes the limiter. The host tiling exists precisely to find the point between these two extremes for a given shape.

## Two Failure Modes Compared

| Aspect | Tiling too small (this page) | Tiling too large (pattern-memory-bound) |
|---|---|---|
| Bottleneck | Loop + sync overhead, idle Cube | GM bandwidth, MTE saturated |
| Cube utilization | Low on a compute-bound shape | Low because compute starves on data |
| MTE profile | Many short bursts | Few long bursts at >90% bandwidth |
| Root signal | tile dims < fractal / under-fill L0/L1 | tile footprint > UB/L1 budget, spills |
| Fix direction | **Grow** tiles toward L0/L1/UB | **Shrink** tiles, add data reuse |
| Shared tool | Host tiling (technique-tiling-strategy) picks the balance point | same |

## Trade-offs, Pitfalls, and Notes

- **Do not grow blindly.** Each step toward larger tiles reduces overhead but increases the UB/L1 footprint. Always leave room for the second buffer; otherwise you trade an overhead problem for the serialization described in pattern-pipeline-stall.
- **Alignment first, size second.** A perfectly sized but unaligned tile still wastes a partial fractal every iteration. Fix `% 16` alignment before tuning magnitude.
- **Trust the host tiling for variable shapes.** Hard-coded tiles that are correct for one `M, N, K` are usually too small (or too large) for another. The AscendC Tiling API and Catlass exist to keep the tile proportional to the shape; prefer them over literals, consistent with technique-tiling-strategy.
- **Confirm the shape really is compute-bound.** If the FLOP/byte ratio is low, the kernel was memory-bound all along and growing tiles will not help — re-route to pattern-memory-bound.
- **Confidence:** this page is `source-reported`; the mechanism and the "grow to fill L0/L1/UB, align to 16, balance via host tiling" guidance come from doc-ascendc-tiling-api and doc-catlass-framework. No specific utilization or speedup numbers are claimed here because none are reported for this pattern.

## Related Patterns

- [Low Cube Utilization](pattern-low-cube-utilization) — the broader pattern this is a sub-case of
- [Tiling Strategy](technique-tiling-strategy) — host-side tile selection that picks the balance point
- [Memory-Bound Kernel](pattern-memory-bound) — the opposite extreme reached by over-growing tiles
- [Cube Unit](hw-cube-unit) — the 16×16 fractal and L0/L1 buffers that set the target tile size
