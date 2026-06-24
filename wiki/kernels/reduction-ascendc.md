---
id: kernel-reduction-ascendc
title: "Reduction Operations (ReduceSum/ReduceMax) on Ascend NPU"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [reduce, reduction, vector-unit, ascendc]
confidence: source-reported
kernel_types: [reduce]
languages: [ascendc]
related: [wiki-hardware-vector-unit, kernel-layernorm-ascendc]
sources: [doc-ascendc-api-reference, blog-cann-training-camp]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp32
    shape: "elements=1048576"
    metric: GB/s
    value: 200
    utilization: "~65%"
    source_id: blog-cann-training-camp
reproducibility: snippet
techniques: [data-reuse]
---

# Reduction Operations (ReduceSum/ReduceMax) on Ascend NPU

## Overview

Reduction operations (ReduceSum, ReduceMax, ReduceMin, ReduceMean) are fundamental parallel primitives used throughout deep learning models. These operations appear in LayerNorm, Softmax, attention mechanisms, and gradient computations. On Ascend NPU, reductions are primarily executed on the Vector unit, with optimized APIs for common reduction patterns.

## AscendC Reduction APIs

AscendC provides native APIs for reduction operations on the Vector unit:

```ascendc
// Sum reduction
ReduceSum(dst, src, count);

// Maximum reduction
ReduceMax(dst, src, count);

// Minimum reduction
ReduceMin(dst, src, count);

// Mean reduction (sum + scale)
ReduceMean(dst, src, count);
```

These APIs handle the complex reduction logic across Vector unit processing elements, managing intra-core and inter-core communication transparently.

## Hierarchical Reduction Strategy

For large reductions exceeding Vector unit capacity, a hierarchical approach is employed:

**Level 1: Per-AICore Partial Reduction**
```ascendc
// Each AICore processes a tile of data
LocalTensor<float> local_sum = BufferPool::Alloc();
ReduceSum(local_sum, input_tile, tile_size);
```

**Level 2: Cross-Core Reduction via GM**
```ascendc
// Accumulate partial results across AICores
__gm__float* partial_sums;  // [num_cores]
// Final reduction across partial results
```

This two-level approach balances computation and communication, minimizing cross-core synchronization while maintaining high utilization.

## Implementation Example: Row-wise ReduceSum

```ascendc
extern "C" __global__ void RowWiseReduceSum(
    __gm____half__* input,      // [rows, cols]
    __gm____half__* output,     // [rows]
    int rows, int cols
) {
    LocalTensor<Half> input_ub = BufferPool::Alloc();
    LocalTensor<Half> sum_ub = BufferPool::Alloc();
    
    for (int row = 0; row < rows; ++row) {
        // Copy row to UB
        DataCopy(input_ub, input + row * cols, cols);
        
        // Vector unit reduction
        ReduceSum(sum_ub, input_ub, cols);
        
        // Copy result back
        DataCopy(output + row, sum_ub, 1);
    }
    
    BufferPool::Dealloc(input_ub);
    BufferPool::Dealloc(sum_ub);
}
```

## Key Optimization Considerations

**Vector Unit Tile Processing**: The Vector unit processes data in tiles, so reductions across tiles require UB accumulation:

```ascendc
// Multi-tile reduction for large arrays
LocalTensor<Half> accumulator = BufferPool::Alloc();
for (int tile = 0; tile < num_tiles; ++tile) {
    LocalTensor<Half> tile_sum = BufferPool::Alloc();
    ReduceSum(tile_sum, input_ub + tile * tile_size, tile_size);
    Add(accumulator, accumulator, tile_sum, 1);
    BufferPool::Dealloc(tile_sum);
}
```

**Data Type Considerations**: Higher precision accumulators prevent overflow for fp16 inputs:
```ascendc
// Use fp32 accumulator for fp16 input reduction
LocalTensor<Float> fp32_accum = BufferPool::Alloc();
ReduceSum(fp32_accum, fp16_input, count);
```

**Memory Access Patterns**: Coalesced GM access and efficient UB buffer reuse are critical for performance:
```ascendc
// Good: Sequential access pattern
DataCopy(input_ub, gm_input + offset, tile_size);

// Avoid: Strided access pattern
for (int i = 0; i < count; i += stride) {
    // Poor memory coalescing
}
```

## Performance Characteristics

On Ascend 910B with fp32 precision:
- ReduceSum throughput: ~200 GB/s (~65% theoretical peak)
- ReduceMax throughput: ~180 GB/s (~60% theoretical peak)
- Performance scales with tile size due to amortized memory access overhead

## Integration with Other Operations

Reductions are fundamental building blocks for complex operations:

**LayerNorm**: Uses ReduceSum for mean and variance computation
```ascendc
ReduceSum(mean_ub, input_ub, hidden_dim);
```

**Softmax**: Uses ReduceMax for numerical stability
```ascendc
ReduceMax(max_ub, logits_ub, vocab_size);
Sub(exp_ub, logits_ub, max_ub, vocab_size);  // x - max(x)
```

**Attention**: Uses ReduceSum for attention weights normalization
```ascendc
ReduceSum(sum_ub, scores_ub, seq_len);
Div(weights_ub, scores_ub, sum_ub, seq_len);
```

## Comparison with GPU Reduction

Compared with CUDA reduction implementations:
- **Programming Model**: AscendC provides higher-level reduction APIs vs. CUDA's explicit warp/block primitives
- **Performance**: Comparable bandwidth utilization, with Ascend showing advantages for specific reduction patterns
- **Optimization**: Both require careful memory access pattern design for optimal performance

The Ascend reduction implementation demonstrates how specialized Vector unit APIs can simplify common parallel reduction patterns while maintaining high performance.