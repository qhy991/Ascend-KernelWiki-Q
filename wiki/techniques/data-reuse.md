---
id: technique-data-reuse
title: "UB Data Reuse — Minimizing GM Bandwidth Pressure"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [data-reuse, unified-buffer, memory, optimization]
confidence: source-reported
techniques: [data-reuse]
hardware_features: [unified-buffer, mte]
kernel_types: [gemm, attention, softmax, layernorm]
related: [hw-unified-buffer, technique-double-buffering, technique-pipeline-scheduling]
sources: [doc-ascend-memory-hierarchy, blog-cann-training-camp]
reproducibility: concept
---

# UB Data Reuse — Minimizing GM Bandwidth Pressure

A fundamental optimization principle on Ascend architectures is maximizing data reuse within the Unified Buffer (UB) to minimize expensive Global Memory (GM) transfers. GM accesses have 3-5× higher latency than UB accesses and create bandwidth pressure that limits scalability.

## Core Principle

**Keep data in UB as long as possible.** Each GM transfer should be amortized over multiple compute operations.

## Data Reuse Strategies

### 1. Cross-Tile Reuse in Attention
For Q×K^T×V attention computation, the Q tensor can be reused across all K and V tiles:

```
for each Q_tile:
    Load Q_tile into UB (once)
    for each K_tile:
        Compute Q_tile × K_tile^T
    for each V_tile:
        Compute attention_weights × V_tile
```

This reduces GM transfers from O(N²) to O(N) for the Q tensor.

### 2. In-Place LayerNorm Computation
LayerNorm operations can reuse activation tensors efficiently:
1. Load activation tensor once into UB
2. Compute mean and variance in single pass
3. Normalize in-place using the same UB allocation
4. Write final result back to GM

### 3. Pipelined Tile Overlap
While computing on current tile, preload next tile using MTE (Memory Transfer Engine):

```cpp
// AscendC pseudo-code
UB_tile_current = compute(Tile_N);
MTE_async(Tile_N+1);  // Overlapped transfer
UB_tile_next = wait_for_MTE();
```

This hides GM latency behind compute operations.

## UB Budget Planning

Each AICore has ~1-2 MB of UB. Typical allocation for GEMM:

| Component | Size (bytes) | Notes |
|-----------|--------------|-------|
| Tile A | 256 × 256 × 4 = 256K | FP32, can use FP16 |
| Tile B | 256 × 256 × 4 = 256K | FP32, can use FP16 |
| Tile C | 256 × 256 × 4 = 256K | Accumulator, FP32 |
| Double buffer | ~768K | For overlap scheduling |
| Scratch/Temp | ~128K | For intermediate results |
| **Total** | **~1.4M** | Fits within 2MB UB |

Careful budget planning enables aggressive data reuse without UB capacity overruns.