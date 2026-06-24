---
id: kernel-softmax-ascendc
title: "AscendC Softmax — Vector Unit Implementation"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [softmax, vector-unit, reduction, ascendc]
confidence: source-reported
kernel_types: [softmax]
languages: [ascendc]
related: [wiki-hardware-vector-unit, technique-pipeline-scheduling]
sources: [doc-ascendc-api-reference, blog-cann-training-camp]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp32
    shape: "rows=4096, cols=4096"
    metric: GB/s
    value: 120
    utilization: "~60%"
    source_id: blog-cann-training-camp
reproducibility: snippet
techniques: [pipeline-scheduling]
---

# AscendC Softmax on Vector Unit

Softmax on Ascend NPU is implemented using Vector Unit operations for elementwise arithmetic and reductions. The three-pass algorithm—find maximum, exponentiate and sum, then normalize—requires careful use of Vector APIs to achieve numerical stability and performance.

## Three-Pass Algorithm

### Pass 1: Find Maximum
```cpp
void SoftmaxPass1_Max(LocalTensor<float>& input, LocalTensor<float>& max_vals, 
                     int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        // ReduceMax over each row
        auto row = input[i * cols];
        ReduceMax(max_vals[i], row, cols);
    }
}
```

### Pass 2: Exponentiate and Sum
```cpp
void SoftmaxPass2_ExpSum(LocalTensor<float>& input, LocalTensor<float>& max_vals,
                         LocalTensor<float>& exp_vals, LocalTensor<float>& sum_vals,
                         int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        // Subtract max for numerical stability: x - max(x)
        Sub(input[i * cols], max_vals[i], exp_vals[i * cols], cols);
        
        // Exponentiate: exp(x - max)
        Exp(exp_vals[i * cols], exp_vals[i * cols], cols);
        
        // Sum exponents: sum(exp(x - max))
        ReduceSum(exp_vals[i * cols], sum_vals[i], cols);
    }
}
```

### Pass 3: Normalize
```cpp
void SoftmaxPass3_Normalize(LocalTensor<float>& exp_vals, LocalTensor<float>& sum_vals,
                           LocalTensor<float>& output, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        // Compute reciprocal of sum
        LocalTensor<float> inv_sum;
        Reciprocal(sum_vals[i], inv_sum, 1);
        
        // Normalize: exp(x) / sum(exp(x))
        Mul(exp_vals[i * cols], inv_sum, output[i * cols], cols);
    }
}
```

## Complete AscendC Softmax Kernel

```cpp
extern "C" __global__ __aicore__ void softmax_kernel(
    __gm__ uint8_t* GM_input, __gm__ uint8_t* GM_output,
    int rows, int cols) {
    
    TPipe pipe;
    
    // Allocate Unified Buffer for input, intermediates, output
    auto input = AllocUB<float>(rows * cols);
    auto max_vals = AllocUB<float>(rows);
    auto exp_vals = AllocUB<float>(rows * cols);
    auto sum_vals = AllocUB<float>(rows);
    auto output = AllocUB<float>(rows * cols);
    
    // Load input from Global Memory
    DataCopy(input, GM_input, rows * cols);
    
    // Pipeline the three passes with overlapping
    pipe.InitBuffer(input, exp_vals, output);
    
    for (int i = 0; i < rows; i++) {
        // Pass 1: Find max (Vector Queue)
        pipe.ReduceMax(input + i * cols, max_vals + i, cols);
    }
    
    for (int i = 0; i < rows; i++) {
        // Pass 2: Subtract max, exp, sum (Vector Queue)
        pipe.Sub(input + i * cols, max_vals + i, exp_vals + i * cols, cols);
        pipe.Exp(exp_vals + i * cols, exp_vals + i * cols, cols);
        pipe.ReduceSum(exp_vals + i * cols, sum_vals + i, cols);
    }
    
    for (int i = 0; i < rows; i++) {
        // Pass 3: Normalize (Vector Queue)
        auto inv_sum = AllocUB<float>(1);
        pipe.Reciprocal(sum_vals + i, inv_sum, 1);
        pipe.Mul(exp_vals + i * cols, inv_sum, output + i * cols, cols);
    }
    
    // Write result to Global Memory
    DataCopy(GM_output, output, rows * cols);
}
```

## Numerical Stability

The key to stable softmax is subtracting the maximum before exponentiation:

```
Naïve:    softmax(x) = exp(x) / sum(exp(x))
Stable:   softmax(x) = exp(x - max(x)) / sum(exp(x - max(x)))
```

Without max subtraction, `exp(x)` can overflow for large x (e.g., x > 88 for fp32). By subtracting max first, we ensure `exp(x - max) ≤ 1`.

## Optimization: Fuse into Single Stage

For better performance, fuse all three passes into a single pipeline stage:

```cpp
void FusedSoftmax(LocalTensor<float>& input, LocalTensor<float>& output, 
                 int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        // Find max
        auto max_val = AllocUB<float>(1);
        ReduceMax(input[i * cols], max_val, cols);
        
        // Compute exp(x - max)
        auto centered = AllocUB<float>(cols);
        Sub(input[i * cols], max_val, centered, cols);
        Exp(centered, centered, cols);
        
        // Sum and normalize
        auto sum_val = AllocUB<float>(1);
        ReduceSum(centered, sum_val, cols);
        Reciprocal(sum_val, sum_val, 1);
        Mul(centered, sum_val, output[i * cols], cols);
    }
}
```

## Performance Characteristics

| Configuration    | Rows × Cols | Data Type | GB/s  | Utilization | Notes                        |
|------------------|-------------|-----------|-------|--------------|------------------------------|
| Ascend 910B      | 4096 × 4096 | fp32      | 120   | ~60%         | Fused single-stage variant   |
| Ascend 910B      | 2048 × 2048 | fp32      | 115   | ~58%         | Smaller dataset              |
| Ascend 910B      | 4096 × 4096 | fp16      | 95    | ~48%         | FP16 has lower throughput    |

## Vector Unit API Reference

Key AscendC Vector APIs for softmax:

- **ReduceMax**: `ReduceMax(LocalTensor& dst, LocalTensor& src, int count)` — Find maximum over count elements
- **Sub**: `Sub(LocalTensor& dst, LocalTensor& src1, LocalTensor& src2, int count)` — Elementwise subtraction
- **Exp**: `Exp(LocalTensor& dst, LocalTensor& src, int count)` — Elementwise exponentiation
- **ReduceSum**: `ReduceSum(LocalTensor& dst, LocalTensor& src, int count)` — Sum over count elements
- **Reciprocal**: `Reciprocal(LocalTensor& dst, LocalTensor& src, int count)` — Elementwise reciprocal
- **Mul**: `Mul(LocalTensor& dst, LocalTensor& src1, LocalTensor& src2, int count)` — Elementwise multiplication

## Pipeline Integration

Softmax can be fused with preceding matmul (e.g., in attention kernels) to avoid GM reads/writes:

```cpp
// Attention: softmax(Q@K^T) as fused kernel
Matmul(S, Q, K, {M, N, d});        // Cube Unit
SoftmaxInPlace(S, {M, N});         // Vector Unit (fused)
Matmul(O, S, V, {M, d, N});       // Cube Unit
```

This fusion eliminates intermediate storage for `S` and enables better Cube/Vector overlap.
