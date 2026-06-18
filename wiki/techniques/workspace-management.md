---
id: technique-workspace-management
title: "Workspace Management — UB Budgeting and GM Scratch Tensors"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [workspace-management, memory, ub, optimization]
confidence: source-reported
techniques: [workspace-management]
hardware_features: [unified-buffer, global-memory, l1-buffer]
kernel_types: [matmul, attention, layernorm]
related: [hw-unified-buffer, technique-double-buffering, technique-tiling-strategy]
sources: [doc-ascendc-tiling-api, doc-ascend-memory-hierarchy, doc-ascendc-api-reference]
reproducibility: snippet
---

# Workspace Management — UB Budgeting and GM Scratch Tensors

Workspace management is the discipline of fitting every concurrently-live tensor into the limited on-chip Unified Buffer (UB) while spilling anything too large to a Global Memory (GM) scratch tensor. On an Ascend 910B-class core the UB budget is roughly 192KB–256KB, and every `TQue`/`TBuf` tile allocated through `TPipe` competes for that space. Getting the budget right is the difference between a kernel that compiles and one that silently corrupts data or fails allocation at launch.

## The UB Budget

The UB is the working scratchpad for the Vector and (via the L1/L0 path) Cube pipelines. All tiles that are *alive at the same time* must coexist in it:

- Input staging tiles (`QuePosition::VECIN`)
- Output staging tiles (`QuePosition::VECOUT`)
- Intermediate scratch (`TPosition::VECCALC` via `TBuf`)
- Reduction accumulators, masks, and temporaries

The constraint is a simple sum over the live set:

```
sum(byteSize_i × bufNum_i) ≤ UB_CAPACITY   (≈192KB–256KB on 910B class)
```

The `bufNum` argument to `InitBuffer` is where double buffering enters the budget. A queue declared with `bufNum = 2` reserves *two* physical tiles so the MTE engine can fill tile k+1 while compute drains tile k. That doubles the footprint of every double-buffered operand — see technique-double-buffering for the overlap mechanism this pays for. If the doubled live set no longer fits, you must shrink the tile shape, which couples workspace management tightly to technique-tiling-strategy.

### Sizing example

For a vector kernel staging two `half` inputs and one output, each `totalLength` elements, with single buffering:

```
3 × totalLength × sizeof(half) = 3 × totalLength × 2 bytes
```

With double buffering on all three queues the requirement doubles to `6 × totalLength × 2`. Picking `totalLength` per tile is therefore a budget calculation, not a free choice; the host tiling code is responsible for choosing a `totalLength` that keeps the doubled sum under capacity.

## TPipe and TBuf Allocation

In AscendC, `TPipe` owns the UB and hands out tiles. Queues (`TQue`) carry data across pipeline stages; `TBuf` provides un-queued scratch that you read and write in place.

```cpp
#include "kernel_operator.h"
using namespace AscendC;

class LayerNormKernel {
public:
    __aicore__ inline void Init(GM_ADDR x, GM_ADDR gamma, GM_ADDR y,
                                GM_ADDR workspace, uint32_t tileLen) {
        xGm.SetGlobalBuffer((__gm__ half*)x);
        yGm.SetGlobalBuffer((__gm__ half*)y);
        // GM scratch handed in by the host; see GM Workspace below.
        wsGm.SetGlobalBuffer((__gm__ float*)workspace);

        this->tileLen = tileLen;

        // Double-buffered staging queues (bufNum = 2 -> 2x footprint).
        pipe.InitBuffer(inQueueX,  2, tileLen * sizeof(half));
        pipe.InitBuffer(outQueueY, 2, tileLen * sizeof(half));

        // Single-buffered scratch tiles reused across the phase.
        pipe.InitBuffer(meanBuf, tileLen * sizeof(float));
        pipe.InitBuffer(tmpBuf,  tileLen * sizeof(float));
    }

private:
    TPipe pipe;
    TQue<QuePosition::VECIN,  2> inQueueX;
    TQue<QuePosition::VECOUT, 2> outQueueY;
    TBuf<TPosition::VECCALC>     meanBuf;   // reduction accumulator
    TBuf<TPosition::VECCALC>     tmpBuf;    // reused scratch

    GlobalTensor<half>  xGm, yGm;
    GlobalTensor<float> wsGm;               // GM workspace
    uint32_t tileLen;
};
```

The two `InitBuffer` overloads are the workhorses: `InitBuffer(que, bufNum, byteSize)` for queues that need ping-pong depth, and `InitBuffer(buf, byteSize)` for a flat `TBuf` scratch tile.

### Reusing Buffers Across Phases

A `TBuf` is not tied to a single use. If a kernel has a reduction phase and a normalization phase that never overlap in time, the same `tmpBuf` can hold the per-row max during phase one and the reciprocal-norm during phase two. Because only the *live* set counts against the budget, folding two non-overlapping temporaries into one `TBuf` directly buys back UB capacity for larger tiles. This is the cheapest workspace optimization available and should be the first lever you reach for before adding GM spill.

## GM Workspace — Off-Chip Scratch

When an intermediate is too large for the UB — split-K partial sums, a full attention score block, or a long-axis reduction that cannot be tiled away — it lives in a GM scratch tensor instead. The pattern, documented in doc-ascendc-tiling-api, is:

1. **Host** computes the scratch byte size during tiling and requests it as the kernel's workspace.
2. The runtime allocates that GM region and passes its address into the kernel as an extra `GM_ADDR workspace` parameter.
3. **Kernel** wraps it with `SetGlobalBuffer` and treats it as ordinary global memory: `DataCopy` UB tiles in and out of it across phases.

```cpp
// Host-side tiling: size the GM scratch for split-K partials.
size_t splitKPartials = blockNum * tileM * tileN * sizeof(float);
tilingData.set_workspaceSize(splitKPartials);
// The framework forwards this size to the runtime, which provides
// the matching GM_ADDR workspace to the kernel at launch.
```

Inside the kernel, split-K accumulation writes each K-slice partial to `wsGm`, then a final reduction phase reads all partials back. GM bandwidth is far lower than UB, so workspace traffic is a real cost — it is justified only when the alternative (keeping everything resident in UB) is impossible.

### Auto Workspace

Newer CANN releases support *auto workspace*: rather than the kernel author hand-computing the scratch size, the AscendC tiling API can derive a default system workspace and the framework reserves it automatically. Authors still allocate any *user* workspace they need through the tiling data, but the boilerplate of plumbing a baseline scratch region is handled for you. The contract at the kernel boundary is unchanged — the scratch still arrives as a `GM_ADDR` and is wrapped with `SetGlobalBuffer`.

## UB vs GM Workspace

| Property            | UB (`TQue`/`TBuf`)              | GM workspace (`GM_ADDR`)            |
|---------------------|--------------------------------|-------------------------------------|
| Capacity            | ~192KB–256KB / core (910B)     | Bounded by device HBM               |
| Bandwidth           | Highest (on-chip)              | Lowest (off-chip HBM)               |
| Sized by            | Tile shape × `bufNum`          | Host tiling (`workspaceSize`)       |
| Passed to kernel as | Allocated by `TPipe`           | Extra `GM_ADDR workspace` param     |
| Typical use         | Live staging + small scratch   | Split-K partials, oversized inter.  |
| Double buffering    | Doubles footprint              | N/A (resident, not ping-ponged)     |

## Trade-offs and Pitfalls

**Advantages of disciplined budgeting:**
- Prevents allocation failures and silent overwrites from over-subscribing the UB.
- Reusing `TBuf` across phases reclaims capacity for larger, more efficient tiles.
- GM spill makes otherwise-impossible shapes (large split-K, long reductions) runnable.

**Pitfalls:**
- **Forgetting the `bufNum` multiplier.** A queue at `bufNum = 2` costs twice its tile size. Budgeting against the single-buffer figure is the most common cause of over-subscription.
- **Counting peak live set, not total allocation.** Tiles that never coexist do not sum; tiles that do must all fit simultaneously. Misjudging the *concurrent* set either wastes UB or overflows it.
- **Over-spilling to GM.** Because GM bandwidth is the bottleneck, pushing data that *could* tile into UB out to a workspace tensor can make a kernel memory-bound. Spill only what genuinely cannot fit.
- **Stale host/kernel workspace contract.** If the host under-sizes `workspaceSize` relative to what the kernel writes, the kernel scribbles past its scratch region. The host tiling size and the kernel's GM access pattern must agree exactly.

## Notes

Workspace management is the connective tissue between technique-tiling-strategy (which chooses the shapes) and technique-double-buffering (which multiplies their cost). Concrete uses appear in the matmul and attention kernels of this knowledge base — for example, split-K GM partials in matmul-ascendc and per-row reduction scratch in layernorm-style kernels. The exact UB capacity is hardware-specific (consult hw-unified-buffer for per-architecture figures); treat the 192KB–256KB range as the 910B-class working assumption, not a universal constant.
