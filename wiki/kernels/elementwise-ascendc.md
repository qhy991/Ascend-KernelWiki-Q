---
id: kernel-elementwise-ascendc
title: "Elementwise Operations — AscendC Vector Template"
type: wiki-kernel
architectures: [ascend910, ascend910b, ascend310p]
tags: [elementwise, vector-unit, activation, ascendc]
confidence: verified
kernel_types: [elementwise, activation]
languages: [ascendc]
related: [hw-vector-unit, technique-pipeline-scheduling]
sources: [doc-ascendc-api-reference, blog-ascendc-programming-guide]
reproducibility: snippet
techniques: [pipeline-scheduling]
---

# Elementwise Operations — AscendC Vector Template

## Overview

Elementwise operations form the foundation of neural network computations, including arithmetic operations (Add, Sub, Mul, Div) and activation functions (ReLU, Sigmoid, GELU, Silu). On Ascend NPU, these operations are efficiently executed on the Vector unit using a template-based programming approach that provides type generality and code reusability.

## Kernel Template Pattern

The AscendC elementwise kernel follows a consistent three-stage pattern applicable to most elementwise operations:

**Stage 1: CopyIn (GM → UB)**
```ascendc
// Transfer data from Global Memory to Unified Buffer
DataCopy(ub_buffer, gm_input, tile_size);
```

**Stage 2: Vector Operation (UB computation)**
```ascendc
// Perform elementwise operation in UB
Add(ub_output, ub_input1, ub_input2, tile_size);  // Binary operation
Relu(ub_output, ub_input, tile_size);              // Unary operation
```

**Stage 3: CopyOut (UB → GM)**
```ascendc
// Transfer result back to Global Memory
DataCopy(gm_output, ub_output, tile_size);
```

This pattern enables efficient memory access and computation overlap through pipeline scheduling.

## Generic Unary Operation Kernel Template

```ascendc
template<typename UnaryOp>
extern "C" __global__ void UnaryElementwiseKernel(
    __gm____half__* input,
    __gm____half__* output,
    int total_elements
) {
    const int tile_size = 1024;  // Optimal tile size for UB
    
    LocalTensor<Half> input_ub = BufferPool::Alloc();
    LocalTensor<Half> output_ub = BufferPool::Alloc();
    
    int num_tiles = (total_elements + tile_size - 1) / tile_size;
    
    for (int tile_idx = 0; tile_idx < num_tiles; ++tile_idx) {
        int offset = tile_idx * tile_size;
        int current_tile_size = min(tile_size, total_elements - offset);
        
        // CopyIn stage
        DataCopy(input_ub, input + offset, current_tile_size);
        
        // Computation stage
        UnaryOp::Apply(output_ub, input_ub, current_tile_size);
        
        // CopyOut stage
        DataCopy(output + offset, output_ub, current_tile_size);
    }
    
    BufferPool::Dealloc(input_ub);
    BufferPool::Dealloc(output_ub);
}
```

## Supported Operations

**Arithmetic Operations**:
- Binary: Add, Sub, Mul, Div, Max, Min, Pow
- Unary: Neg, Abs, Reciprocal, Square, Sqrt

**Activation Functions**:
- ReLU: `Relu(output, input, count)`
- LeakyReLU: `Muls(output, input, alpha, count)` with conditional
- Sigmoid: `Sigmoid(output, input, count)`
- GELU: `Gelu(output, input, count)`
- Silu: `Mul(output, input, Sigmoid(input, count), count)`

## Activation Function Implementations

**ReLU**:
```ascendc
struct ReLUOp {
    static void Apply(LocalTensor<Half>& output, 
                     LocalTensor<Half>& input, 
                     int count) {
        // ReLU: max(0, x)
        Muls(output, input, 1.0f, count);  // Copy
        // Vector unit conditional max with 0
        auto zero = 0.0_h;
        for (int i = 0; i < count; ++i) {
            output[i] = (input[i] > zero) ? input[i] : zero;
        }
    }
};
```

**GELU**:
```ascendc
struct GELUOp {
    static void Apply(LocalTensor<Half>& output, 
                     LocalTensor<Half>& input, 
                     int count) {
        // GELU: x * Φ(x) where Φ is CDF of standard normal
        // Approximation: 0.5 * x * (1 + tanh(√(2/π) * (x + 0.044715 * x^3)))
        
        LocalTensor<Half> x_cubed = BufferPool::Alloc();
        Mul(x_cubed, input, input, count);
        Mul(x_cubed, x_cubed, input, count);
        
        LocalTensor<Half> tanh_input = BufferPool::Alloc();
        Muls(tanh_input, x_cubed, 0.044715f, count);
        Add(tanh_input, tanh_input, input, count);
        Muls(tanh_input, tanh_input, 0.797884f, count);  // √(2/π)
        
        LocalTensor<Half> tanh_output = BufferPool::Alloc();
        Tanh(tanh_output, tanh_input, count);
        
        Add(output, tanh_output, 1.0f, count);
        Muls(output, output, 0.5f, count);
        Mul(output, output, input, count);
        
        BufferPool::Dealloc(x_cubed);
        BufferPool::Dealloc(tanh_input);
        BufferPool::Dealloc(tanh_output);
    }
};
```

## Performance Optimization Techniques

**Pipeline Scheduling**: Overlap memory transfer and computation:
```ascendc
// Async CopyIn for next tile while computing current tile
PipeLine pipeline;
pipeline.CopyIn(next_input_ub, gm_input + next_offset, tile_size);
// Compute current tile
UnaryOp::Apply(current_output_ub, current_input_ub, tile_size);
pipeline.CopyOut(gm_output + current_offset, current_output_ub, tile_size);
pipeline.Wait();
```

**Vector Unit Utilization**: Process multiple elements per cycle:
```ascendc
// Vector unit processes 256 elements per cycle on Ascend 910B
const int vector_length = 256;  
int vector_ops = (tile_size + vector_length - 1) / vector_length;
```

**Data Reuse**: In-place operations minimize UB memory usage:
```ascendc
// Reuse input buffer for output when operation allows
LocalTensor<Half> buffer = BufferPool::Alloc();
DataCopy(buffer, gm_input, tile_size);
Relu(buffer, buffer, tile_size);  // In-place
DataCopy(gm_output, buffer, tile_size);
```

## Performance Characteristics

On Ascend 910B:
- **fp16 arithmetic**: ~400 GB/s (~80% theoretical peak)
- **fp32 arithmetic**: ~200 GB/s (~75% theoretical peak)
- **activation functions**: ~150-300 GB/s depending on complexity

Performance is primarily bandwidth-bound for simple operations (Add, Mul) and compute-bound for complex activations (GELU, Sigmoid).

## Comparison with GPU Elementwise Operations

Compared with CUDA elementwise kernels:
- **Programming Model**: AscendC provides higher-level Vector APIs vs. CUDA's explicit thread programming
- **Performance**: Comparable bandwidth utilization, with both architectures being bandwidth-bound for elementwise operations
- **Optimization**: Both benefit from memory access coalescing and operation fusion

The Ascend elementwise implementation demonstrates how template-based programming on the Vector unit can provide type-safe, reusable code while maintaining high performance across diverse elementwise operations.