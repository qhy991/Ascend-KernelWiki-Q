---
id: hw-vector-unit
title: "Vector Unit — SIMD Processing Engine"
type: wiki-hardware
architectures: [ascend910, ascend910b, ascend310p]
tags: [vector-unit, simd, compute, hardware]
confidence: verified
hardware_features: [vector-unit]
related: [hw-cube-unit, hw-unified-buffer]
sources: [doc-cann-architecture-guide, doc-ascendc-api-reference]
cuda_equivalent: cuda_core
---

# Vector Unit — SIMD Processing Engine

The Vector Unit is Ascend's SIMD (Single Instruction, Multiple Data) processing engine, analogous to CUDA cores in NVIDIA GPUs. It handles element-wise operations, reductions, and activation functions that complement the Cube Unit's matrix operations.

## Core Functionality

The Vector Unit processes data in parallel vectors, accelerating operations that are not matrix-multiplication bound:

**Element-wise Operations**:
- Arithmetic: `Add`, `Mul`, `Sub`, `Div`, `Sqrt`, `Pow`
- Comparison: `Greater`, `Less`, `Equal`, `LogicalAnd`, `LogicalOr`
- Rounding: `Floor`, `Ceil`, `Round`

**Reductions**:
- `ReduceSum`, `ReduceMax`, `ReduceMin`, `ReduceMean`
- Supports reduction along arbitrary dimensions

**Activation Functions**:
- `Softmax`, `ReLU`, `Sigmoid`, `Tanh`, `GELU`
- Layer normalization operations

## Supported Data Types

- **Floating Point**: FP16, FP32, BF16
- **Integer**: INT32, INT8
- **Mixed precision**: Automatic promotion as needed

## Memory Interaction

The Vector Unit operates exclusively on data stored in the **Unified Buffer (UB)**:
- **Input**: Reads operands from UB
- **Output**: Writes results back to UB
- **No direct HBM access**: All data must first be staged to UB via MTE transfers

## Key AscendC APIs

```cpp
// Element-wise operations
Add(lhs, rhs, output);           // Vector addition
Mul(lhs, rhs, output);           // Vector multiplication

// Reductions
ReduceSum(input, output, {axes}); // Sum along specified axes
ReduceMax(input, output, {axes}); // Maximum along axes

// Activation functions
Softmax(input, output, {axes});   // Softmax along axes
ReLU(input, output);              // ReLU activation
```

## Performance Optimization

**Vectorize Tile Operations**:
- Process multiple elements per instruction using SIMD lanes
- Align data accesses to maximize vector unit utilization

**Overlap with Cube Unit**:
- While Cube performs matrix multiply, Vector can handle element-wise post-processing
- Requires careful synchronization across instruction queues

**Memory Efficiency**:
- Keep intermediate results in UB to minimize GM traffic
- Chain multiple Vector operations without writing back to GM

**Pipeline Depth**:
- Vector operations have latency similar to CUDA cores
- Deep pipelines benefit from instruction-level parallelism

## Integration with Cube Unit

Typical deep learning kernels use both units cooperatively:
1. **Cube**: Computes matrix multiplication (GEMM)
2. **Vector**: Applies bias, activation functions, and residual connections
3. **Synchronization**: Event-based sync between Cube and Vector queues

This division of labor enables higher overall throughput than using either unit alone.

## Comparison with CUDA Cores

| Aspect | Ascend Vector Unit | CUDA Cores |
|--------|-------------------|-------------|
| Primary Role | Element-wise operations | General-purpose compute |
| Memory Interface | UB-only | Shared memory + registers |
| SIMD Width | Vector-specific | Warp-wide (32 threads) |
| Integration | Separate queue from Cube | Same pipeline as Tensor Cores |

The separate queue architecture allows Vector and Cube units to operate independently, enabling better overlap than CUDA's shared warp scheduler.
