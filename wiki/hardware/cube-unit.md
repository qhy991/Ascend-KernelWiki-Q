---
id: wiki-hardware-cube-unit
title: "Cube Unit — Matrix Multiply Accelerator (Ascend 910/910B)"
type: wiki-hardware
architectures: [ascend910, ascend910b]
tags: [cube-unit, matrix, compute, hardware]
confidence: verified
hardware_features: [cube-unit]
related: [wiki-hardware-vector-unit, hw-unified-buffer, hw-instruction-queue]
sources: [doc-cann-architecture-guide, doc-ascendc-api-reference, doc-catlass-framework]
cuda_equivalent: tensor_core
---

# Cube Unit — Matrix Multiply Accelerator

The Cube Unit is Ascend's dedicated hardware accelerator for matrix multiplication operations, analogous to NVIDIA's Tensor Cores. It provides high-throughput matrix-matrix and matrix-vector operations essential for deep learning workloads.

## Core Functionality

The Cube Unit accelerates matrix multiply operations across multiple data types:
- **Floating Point**: FP16, BF16, FP32 accumulation
- **Integer**: INT8 with INT32 accumulation
- **Mixed precision**: FP16/BF16 computation with FP32 accumulation

## Programming Interface

**AscendC Matmul API**:
```cpp
// Basic matrix multiply (M=N=K dimensions)
Matmul(lhs, rhs, output, {M, N, K});
```

**Catlass Framework**: Higher-level abstraction providing GEMM kernels with automatic tiling, format conversion, and performance optimization.

## Data Format Requirements

The Cube Unit has a strict data format requirement: **FRACTAL_NZ**, a 5D tiled layout optimized for the Cube's internal dataflow. This format organizes data into fixed-size blocks (16×16 for FP16/BF16, 32×32 for INT8) to maximize memory bandwidth and compute utilization.

**Format Conversion**: Data from standard ND (N-dimensional) format must be converted to FRACTAL_NZ before feeding the Cube:
- AscendC provides `Cast` and `Transpose` APIs for conversion
- Catlass framework handles this automatically
- Conversion overhead can be amortized over multiple operations

## Memory Hierarchy Integration

- **Input Source**: Reads matrix tiles from Unified Buffer (UB)
- **Accumulation**: Maintains partial sums in L0 buffer (internal registers)
- **Output**: Writes results back to UB

## Performance Comparison

| Hardware | Peak Throughput (FP16/BF16) | Power Efficiency |
|----------|----------------------------|-------------------|
| Ascend 910A | ~64 TFLOPS | Baseline |
| Ascend 910B | ~128 TFLOPS | 2x improvement |
| NVIDIA H100 Tensor Core | ~989 TFLOPS (FP8) | Different class |

*Note: Exact throughput depends on problem dimensions and data layout efficiency*

## Key Limitations

1. **Format Restriction**: Only supports FRACTAL_NZ format, requiring explicit conversion from standard ND layouts
2. **Tile Constraints**: Optimal performance requires dimensions that align with 16×16 tiles (FP16/BF16) or 32×32 tiles (INT8)
3. **Size Requirements**: Matrix dimensions must meet minimum thresholds to fully utilize the Cube units
4. **Memory Bandwidth**: Performance limited by UB→Cube bandwidth; requires careful tiling strategies

## Best Practices

- **Prefer FRACTAL_NZ** for frequently accessed tensors to avoid repeated format conversion
- **Tile dimensions** should be multiples of 16/32 for optimal utilization
- **Overlap format conversion** with other operations using the 4-queue architecture
- **Batch small GEMMs** to amortize format conversion overhead
