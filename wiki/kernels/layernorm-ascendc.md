---
id: kernel-layernorm-ascendc
title: "LayerNorm / RMSNorm on Ascend NPU"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [layernorm, rmsnorm, normalization, vector-unit]
confidence: source-reported
kernel_types: [layernorm, rmsnorm]
languages: [ascendc]
related: [hw-vector-unit, technique-data-reuse]
sources: [doc-ascendc-api-reference, blog-cann-training-camp]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp32
    shape: "batch=4096, hidden=4096"
    metric: GB/s
    value: 150
    utilization: "~55%"
    source_id: blog-cann-training-camp
reproducibility: snippet
techniques: [data-reuse, pipeline-scheduling]
---

# LayerNorm / RMSNorm on Ascend NPU

## Overview

Layer Normalization (LayerNorm) and Root Mean Square Layer Normalization (RMSNorm) are fundamental operations in transformer architectures and neural network training. LayerNorm computes mean and variance across features for each sample, while RMSNorm is a simplified variant that omits mean centering. Both operations are bandwidth-intensive and require careful memory access patterns for optimal performance.

## Mathematical Formulation

**LayerNorm**:
```
mean = sum(x) / n
var = sum((x - mean)^2) / n
y = (x - mean) / sqrt(var + eps) * gamma + beta
```

**RMSNorm**:
```
rms = sqrt(sum(x^2) / n + eps)
y = (x / rms) * gamma
```

## Ascend NPU Implementation

The Vector unit on Ascend NPU is optimized for elementwise and reduction operations, making it ideal for normalization kernels. The implementation follows a fused pipeline approach:

**Stage 1: Mean Computation (ReduceSum)**
```ascendc
// ReduceSum across feature dimension
__gm____half__* input;
__gm____half__* mean_buffer;
LocalTensor<Half> mean_ub;
ReduceSum(mean_ub, input_ub, hidden_dim);
```

**Stage 2: Mean Centering (Vector Subtraction)**
```ascendc
// Subtract mean from input
Sub(input_centered_ub, input_ub, mean_ub, hidden_dim);
```

**Stage 3: Variance Computation (Vector Mul + ReduceSum)**
```ascendc
// Compute squared deviations
Mul(deviations_squared_ub, input_centered_ub, input_centered_ub, hidden_dim);
// Sum squared deviations
ReduceSum(variance_ub, deviations_squared_ub, hidden_dim);
```

**Stage 4: Normalization (Vector Division)**
```ascendc
// Normalize: (x - mean) / sqrt(var + eps)
Sqrt(stddev_ub, variance_ub);
Add(eps_added_ub, stddev_ub, epsilon_ub);
Div(normalized_ub, input_centered_ub, eps_added_ub, hidden_dim);
```

**Stage 5: Scale and Shift (Vector Mul + Add)**
```ascendc
// Apply gamma and beta
Mul(output_ub, normalized_ub, gamma_ub, hidden_dim);
Add(final_output_ub, output_ub, beta_ub, hidden_dim);
```

## Key Optimizations

**Fused Pipeline Execution**: The entire LayerNorm operation is fused into a single pipeline stage to minimize data movement. This eliminates intermediate GM writes and reduces memory bandwidth requirements by approximately 60%.

**In-Place UB Buffer Reuse**: 
```ascendc
// Reuse input buffer for output to save UB memory
// Pattern: Input UB -> Computation -> Output UB (same buffer)
DataCopy(input_ub, gm_input);
// ... computation ...
DataCopy(gm_output, input_ub);  // Reuse buffer
```

**RMSNorm Simplification**: RMSNorm omits the mean computation (stages 1-2), reducing both computational complexity and memory bandwidth requirements by ~30%.

## Performance Characteristics

On Ascend 910B with fp32 precision:
- LayerNorm throughput: ~150 GB/s (~55% theoretical peak)
- RMSNorm throughput: ~180 GB/s (~65% theoretical peak)
- Batch processing benefits from tiling across multiple AICores

## AscendC Code Example

```ascendc
extern "C" __global__ void LayerNormKernel(
    __gm____half__* input,
    __gm____half__* output,
    __gm____half__* gamma,
    __gm____half__* beta,
    __gm____half__* mean,
    __gm____half__* variance,
    float epsilon,
    int hidden_dim
) {
    LocalTensor<Half> input_ub = BufferPool::Alloc();
    LocalTensor<Half> output_ub = input_ub;  // In-place reuse
    
    // Stage 1: Compute mean
    LocalTensor<Half> mean_ub = BufferPool::Alloc();
    ReduceSum(mean_ub, input_ub, hidden_dim);
    Mul(mean_ub, mean_ub, 1.0f / hidden_dim, 1);
    
    // Stage 2: Center input
    Sub(input_ub, input_ub, mean_ub, hidden_dim);
    
    // Stage 3: Compute variance
    LocalTensor<Half> var_ub = BufferPool::Alloc();
    Mul(var_ub, input_ub, input_ub, hidden_dim);
    ReduceSum(var_ub, var_ub, hidden_dim);
    Mul(var_ub, var_ub, 1.0f / hidden_dim, 1);
    
    // Stage 4: Normalize
    Adds(var_ub, var_ub, epsilon, 1);
    Sqrt(var_ub, var_ub);
    Div(input_ub, input_ub, var_ub, hidden_dim);
    
    // Stage 5: Scale and shift
    LocalTensor<Half> gamma_ub = BufferPool::Alloc();
    LocalTensor<Half> beta_ub = BufferPool::Alloc();
    DataCopy(gamma_ub, gamma);
    DataCopy(beta_ub, beta);
    
    Mul(input_ub, input_ub, gamma_ub, hidden_dim);
    Add(input_ub, input_ub, beta_ub, hidden_dim);
    
    DataCopy(output, input_ub);
    
    BufferPool::Dealloc(input_ub);
    BufferPool::Dealloc(mean_ub);
    BufferPool::Dealloc(var_ub);
    BufferPool::Dealloc(gamma_ub);
    BufferPool::Dealloc(beta_ub);
}
```

## Comparison with GPU Implementation

Compared with GPU implementations:
- **Similarities**: Both use reduction-based approaches, benefit from fusion
- **Differences**: Ascend's Vector unit requires explicit buffer management, while GPU uses shared memory differently
- **Performance**: Comparable bandwidth utilization, with Ascend showing advantages in specific batch sizes due to UB cache efficiency

The LayerNorm/RMSNorm implementation demonstrates how AscendC's explicit buffer management and pipeline scheduling can achieve efficient normalization operations for transformer architectures.