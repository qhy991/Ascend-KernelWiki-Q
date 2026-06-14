---
id: wiki-kernel-rope-ascendc
title: RoPE (Rotary Positional Embedding) Implementation in Ascend C
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [vector-unit, ascendc, elementwise, math]
confidence: verified
kernel_types: [elementwise, math]
languages: [ascendc]
sources: [doc-ascendc-api-reference]
reproducibility: pseudocode
---

# RoPE (Rotary Positional Embedding)

RoPE is a standard positional encoding technique used in modern LLMs (e.g., LLaMA). It involves applying rotations to pairs of features in the query and key vectors.

## Implementation Details

The implementation primarily utilizes the Vector Unit for trigonometric functions (`Sin`, `Cos`) and basic arithmetic (`Mul`, `Add`, `Sub`).

### Algorithm

For each pair of adjacent features `(x1, x2)` and angle `theta`:
- `y1 = x1 * cos(theta) - x2 * sin(theta)`
- `y2 = x1 * sin(theta) + x2 * cos(theta)`

### Ascend C Approach

Since the layout usually separates the features, we can perform these operations efficiently using Ascend C's Vector operations:
1. Load `x` vectors into Unified Buffer (UB).
2. Generate or load `sin` and `cos` vectors.
3. Use `Mul`, `Add`, and `Sub` instructions to combine them.

```cpp
// Pseudocode for RoPE computation on Vector Unit
LocalTensor<half> x1 = inQueue.DeQue<half>();
LocalTensor<half> x2 = inQueue.DeQue<half>();
LocalTensor<half> sin_theta = inQueue.DeQue<half>();
LocalTensor<half> cos_theta = inQueue.DeQue<half>();

LocalTensor<half> y1 = outQueue.AllocTensor<half>();
LocalTensor<half> y2 = outQueue.AllocTensor<half>();

// Temp buffers
LocalTensor<half> tmp1 = tempQueue.AllocTensor<half>();
LocalTensor<half> tmp2 = tempQueue.AllocTensor<half>();

// y1 = x1 * cos(theta) - x2 * sin(theta)
Mul(tmp1, x1, cos_theta, count);
Mul(tmp2, x2, sin_theta, count);
Sub(y1, tmp1, tmp2, count);

// y2 = x1 * sin(theta) + x2 * cos(theta)
Mul(tmp1, x1, sin_theta, count);
Mul(tmp2, x2, cos_theta, count);
Add(y2, tmp1, tmp2, count);
```

## Optimization Tips
- **Double Buffering**: Overlap the DMA transfers of `x` and `theta` with the compute.
- **Precomputation**: If `sin` and `cos` are static, precompute and keep them in Global Memory or L1, rather than computing `Sin` and `Cos` inside the kernel to save vector cycles.
