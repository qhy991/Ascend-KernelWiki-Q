---
id: kernel-conv-ascendc
title: "Convolution on Ascend NPU — im2col + GEMM Approach"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [conv, convolution, im2col, cube-unit]
confidence: inferred
kernel_types: [conv]
languages: [ascendc]
related: [kernel-matmul-ascendc, hw-cube-unit, technique-nz-tiling]
sources: [doc-ascendc-api-reference, doc-cann-architecture-guide]
reproducibility: concept
techniques: [nz-tiling, data-reuse]
---

# Convolution on Ascend NPU

Convolution on Ascend NPUs typically follows the im2col + GEMM decomposition strategy, leveraging the high-throughput Cube unit for matrix multiplication rather than implementing direct convolution loops.

## Three-Stage Pipeline

1. **im2col (Vector Unit)**: Unfold input feature map into column matrix stored in UB
   - Extract patches of size (K×K×C_in) centered at each output position
   - Arrange patches as columns in a (K²·C_in) × (H_out·W_out) matrix
   
2. **GEMM (Cube Unit)**: Multiply unfolded input with weight matrix
   - Weights arranged as (C_out) × (K²·C_in) in NZ format
   - Output: (C_out) × (H_out·W_out) matrix
   
3. **Reshape (Vector Unit)**: Convert GEMM output back to feature map layout
   - Reshape from (C_out, H_out·W_out) to (C_out, H_out, W_out)
   - Apply bias and activation if needed

## Memory Consideration

im2col significantly increases memory footprint:
- Input: (C_in, H, W) → Output: (K²·C_in, H_out·W_out)
- Memory expansion factor: K² (kernel size squared)
- For 7×7 conv with 256 channels: ~49× memory expansion

## Optimized Paths

**For 1×1 convolutions**: Skip im2col entirely — directly use GEMM since no spatial overlap exists.

**Built-in Operators**: AscendCL provides optimized convolution operators (e.g., `aclnnConv2d`) that use CANN compiler's internal optimizations, often outperforming manual AscendC implementations.

## Data Flow Diagram

```
Input: (C_in, H, W)                 Weights: (C_out, K×K×C_in)
    |                                    |
    v                                    v
[Vector im2col]                     [Format → NZ]
    |                                    |
    v                                    v
Unfolded: (K²·C_in, H_out·W_out)  NZ_Weights: (C_out, K²·C_in)
    |                                    |
    +------------[Cube GEMM]------------+
                       |
                       v
              Output: (C_out, H_out·W_out)
                       |
                       v
              [Vector Reshape → NHWC]
                       |
                       v
              Final: (C_out, H_out, W_out)
```

## Performance Optimization

- **Tiling**: Process output positions in tiles to fit UB capacity
- **Weight reuse**: Keep NZ-formatted weights in UB/L1 for multiple output tiles
- **Fuse im2col+GEMM**: Overlap Vector unfolding with Cube computation for successive tiles

## Comparison with Direct Conv

Direct convolution (sliding window) has lower memory usage but worse arithmetic intensity on Ascend. The im2col+GEMM approach trades memory bandwidth for better Cube utilization.

## Related Patterns

- [MatMul on Ascend](kernel-matmul-ascendc) — core GEMM operation
- [NZ Tiling](technique-nz-tiling) — weight data layout optimization
- [Data Reuse](technique-data-reuse) — weight caching strategies
