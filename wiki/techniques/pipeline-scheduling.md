---
id: technique-pipeline-scheduling
title: "Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [pipeline, scheduling, optimization]
confidence: source-reported
techniques: [pipeline-scheduling]
hardware_features: [instruction-queue, mte, unified-buffer]
kernel_types: [gemm, attention, softmax]
related: [wiki-hardware-instruction-queue, technique-double-buffering, technique-cube-vector-overlap]
sources: [doc-ascendc-api-reference, blog-ascendc-programming-guide, blog-cann-training-camp]
reproducibility: snippet
---

# Pipeline Scheduling in AscendC

Pipeline scheduling is a fundamental optimization technique in AscendC that orchestrates data movement and computation through independent instruction queues. The three-stage pipeline model—CopyIn → Compute → CopyOut—enables overlapping memory transfers with compute operations, maximizing hardware utilization.

## Pipeline Architecture

AscendC's `TPipe` class manages three distinct instruction queues:

- **MTE Queue** (Memory Transfer Engine): Handles GM ↔ UB data movement
- **Cube Queue**: Executes matrix operations on the Cube unit
- **Vector Queue**: Executes elementwise/reduce operations on the Vector unit

These queues operate in parallel, allowing compute to execute while subsequent tiles are being fetched from Global Memory.

## Code Pattern

```cpp
template<typename T>
void PipelineGEMM() {
    TPipe pipe;
    
    // 1. Initialize: Allocate Unified Buffer tiles
    T bufferA[UB_SIZE_A];
    T bufferB[UB_SIZE_B];
    T bufferC[UB_SIZE_C];
    
    // 2. Pipeline stages
    pipe.InitBuffer(bufferA, UB_SIZE_A, bufferB, UB_SIZE_B, bufferC, UB_SIZE_C);
    
    for (int tile = 0; tile < num_tiles; tile++) {
        // CopyIn: Load next tile from GM to UB (MTE queue)
        DataCopy(bufferA, GM_ADDR_A + tile * tile_size);
        DataCopy(bufferB, GM_ADDR_B + tile * tile_size);
        
        // Compute: Matrix operations (Cube/Vector queue)
        pipe.Matmul(bufferA, bufferB, bufferC, M, N, K);
        
        // CopyOut: Write result to GM (MTE queue)
        DataCopy(GM_ADDR_C + tile * tile_size, bufferC);
    }
}
```

## Key Optimizations

1. **Queue Independence**: MTE transfers for tile k+1 can occur while Cube processes tile k
2. **Buffer Management**: `TPipe` template handles buffer allocation and synchronization
3. **Double Buffering**: Combine with double buffering for maximum overlap
4. **Cube/Vector Overlap**: Vector operations (e.g., softmax) can execute while Cube computes matmul

## Comparison with CUDA

Unlike CUDA's cooperative groups, AscendC pipeline scheduling is hardware-managed through dedicated queues. CUDA requires explicit stream management and thread-block synchronization, while AscendC's `TPipe` abstracts queue coordination with simpler APIs.

## Performance Impact

Effective pipeline scheduling can achieve 2-3× throughput improvement over naive synchronous implementations, particularly for large GEMM and attention kernels where memory bandwidth is the primary bottleneck.
