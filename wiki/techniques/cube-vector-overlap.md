---
id: technique-cube-vector-overlap
title: "Cube/Vector Overlap — Exploiting Independent Instruction Queues"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [overlap, compute, optimization]
confidence: inferred
techniques: [cube-vector-overlap]
hardware_features: [cube-unit, vector-unit, instruction-queue]
kernel_types: [attention, softmax]
related: [wiki-hardware-instruction-queue, hw-cube-unit, hw-vector-unit]
sources: [doc-cann-architecture-guide, blog-cann-training-camp]
reproducibility: concept
---

# Cube/Vector Unit Overlap for Compute Parallelism

The Ascend NPU architecture features independent instruction queues for the Cube Unit (matrix operations) and Vector Unit (elementwise/reduce operations). Cube/Vector overlap exploits this parallelism by issuing Vector operations while Cube computations are in-flight, effectively increasing functional unit utilization.

## Hardware Architecture

- **Cube Queue**: Dedicated to matrix multiplication (GEMM) operations
- **Vector Queue**: Handles elementwise arithmetic, reductions, and data type conversions
- **Instruction-Level Parallelism**: Queues execute independently under hardware management

## Overlap Pattern

The key insight is that Vector operations on tile k can execute concurrently with Cube operations on tile k+1:

```
Timeline:
┌─────────────────┬─────────────────┬─────────────────┐
│ Cube: Q@K^T[k]  │ Vector: Softmax │ Cube: Attn@V[k] │
├─────────────────┼─────────────────┼─────────────────┤
│                 │ Cube: Q@K^T[k+1]│ Vector: Softmax │
└─────────────────┴─────────────────┴─────────────────┘
     Concurrent        Independent          Concurrent
```

## Attention Kernel Example

For Flash Attention `softmax(Q@K^T) @ V`:

```cpp
void FlashAttentionOverlap() {
    TPipe pipe;
    
    for (int tile = 0; tile < num_tiles; tile++) {
        // Stage 1: Cube computes Q@K^T for current tile
        pipe.Matmul(bufferQ, bufferK_transpose, bufferAttn, tile_size);
        
        // Stage 2: Vector computes softmax on previous tile result
        // (executes while Cube processes tile+1)
        if (tile > 0) {
            pipe.ReduceMax(bufferAttn_prev, bufferMax, cols);
            pipe.Sub(bufferAttn_prev, bufferMax);           // x - max(x)
            pipe.Exp(bufferAttn_prev);                       // exp(x - max)
            pipe.ReduceSum(bufferAttn_prev, bufferSum);     // sum(exp)
            pipe.Div(bufferAttn_prev, bufferSum);           // normalize
        }
        
        // Stage 3: Cube computes attention@V for previous tile
        if (tile > 0) {
            pipe.Matmul(bufferAttn_prev, bufferV, bufferOutput, tile_size);
        }
        
        // Rotate buffers
        bufferAttn_prev = bufferAttn;
    }
}
```

## Synchronization Considerations

- **Data Dependency**: Vector ops on tile k require Cube ops on tile k to complete
- **Hardware Scheduling**: NPU automatically queues instructions; no explicit barriers needed
- **Buffer Management**: Use double buffering to provide data independence between tiles

## Performance Impact

Cube/Vector overlap is particularly effective for kernels with balanced Cube and Vector workloads:

- **Attention Kernels**: 1.3-1.5× speedup by overlapping softmax with matmul
- **GEMM + Epilogue**: Overlap bias/relu/add with main GEMM loop
- **Softmax-Heavy Workloads**: Up to 2× improvement when reduction dominates runtime

## Limitations

Overlap benefits are constrained by:

1. **Imbalanced Workloads**: If Cube or Vector dominates, overlap has minimal impact
2. **Data Dependencies**: Cannot overlap operations that share input/output buffers
3. **UB Memory Pressure**: Requires sufficient buffer allocation for concurrent tiles

Effective overlap requires kernels designed with explicit partitioning of Cube and Vector stages, typically achieved through tile-based algorithms with buffer management.
