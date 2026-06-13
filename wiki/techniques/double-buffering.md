---
id: technique-double-buffering
title: "Double Buffering — Overlapping Data Transfer with Compute"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [double-buffer, memory, optimization]
confidence: source-reported
techniques: [double-buffering]
hardware_features: [unified-buffer, mte]
kernel_types: [gemm, attention]
related: [hw-unified-buffer, technique-pipeline-scheduling]
sources: [blog-cann-training-camp, doc-ascend-memory-hierarchy]
reproducibility: snippet
---

# Double Buffering for Memory-Compute Overlap

Double buffering is a memory optimization technique that enables complete overlap between data transfer and computation by maintaining two Unified Buffer (UB) tiles for each operand. While compute processes tile k, the MTE engine loads tile k+1 into the alternate buffer, eliminating memory stalls.

## Mechanism

The ping-pong buffer pattern alternates between two buffer sets:

- **Buffer Set 0**: Processes compute on tile k
- **Buffer Set 1**: Loads data for tile k+1 via MTE

After each iteration, buffer roles swap, ensuring continuous pipeline flow.

## AscendC Implementation

```cpp
template<typename T>
void DoubleBufferedGEMM() {
    TPipe pipe;
    
    // Allocate double-buffered UB tiles
    T bufferA[2][UB_SIZE_A];  // Ping-pong buffers
    T bufferB[2][UB_SIZE_B];
    T bufferC[2][UB_SIZE_C];
    
    int buf_idx = 0;
    
    // Prologue: Load first tile
    pipe.InitBuffer(bufferA[0], bufferB[0], bufferC[0]);
    DataCopy(bufferA[0], GM_ADDR_A);
    DataCopy(bufferB[0], GM_ADDR_B);
    
    for (int tile = 0; tile < num_tiles - 1; tile++) {
        buf_idx = tile % 2;
        int next_idx = (tile + 1) % 2;
        
        // Compute on current buffer (Cube queue)
        pipe.Matmul(bufferA[buf_idx], bufferB[buf_idx], bufferC[buf_idx]);
        
        // Load next tile to alternate buffer (MTE queue)
        DataCopy(bufferA[next_idx], GM_ADDR_A + (tile + 1) * tile_size);
        DataCopy(bufferB[next_idx], GM_ADDR_B + (tile + 1) * tile_size);
        
        // Write result (MTE queue)
        DataCopy(GM_ADDR_C + tile * tile_size, bufferC[buf_idx]);
    }
}
```

## Trade-offs

**Advantages:**
- Eliminates compute stalls waiting for memory loads
- Achieves near-peak throughput for bandwidth-bound kernels
- Complements pipeline scheduling for maximum overlap

**Disadvantages:**
- Doubles UB memory footprint (can limit tile sizes)
- Increased code complexity for buffer index management
- Diminishing returns if compute is arithmetic-bound

## Memory Constraints

Unified Buffer size is hardware-limited (e.g., 1MB on Ascend 910B). Double buffering requires careful tile sizing:

- For GEMM M×N×K: tile_M, tile_N, tile_K must satisfy `2 × (tile_M × tile_K + tile_N × tile_K + tile_M × tile_N) × sizeof(T) ≤ UB_CAPACITY`
- May require smaller tiles than single-buffered variants

## Performance Impact

On Ascend 910B, double buffering typically achieves 1.5-2× speedup over synchronous GEMM for large matrices (M,N,K ≥ 2048) where memory transfer dominates execution time. For small matrices, the overhead of buffer management may outweigh benefits.
