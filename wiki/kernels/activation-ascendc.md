---
id: kernel-activation-ascendc
title: "Activation Functions in Ascend C"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [activation, elementwise, vector-unit]
confidence: verified
sources: []
kernel_types: [activation]
languages: [ascendc]
reproducibility: concept
---

# Activation Functions in Ascend C

Activation functions (e.g., ReLU, GELU, Sigmoid) introduce non-linearity into neural networks. In Ascend C, these operations are strictly **element-wise** and are executed entirely by the **Vector Unit**.

## Vector Unit Execution

Because activations do not require cross-element reduction or matrix multiplication, the Cube Unit is completely bypassed. 

The typical pipeline for an activation kernel is:
1. **MTE2 (CopyIn)**: Load a block of the tensor from Global Memory (GM) to the Unified Buffer (UB) in ND format.
2. **Vector Unit (Compute)**: Apply the activation instruction to the UB data.
3. **MTE3 (CopyOut)**: Store the activated block from UB back to GM.

## Ascend C APIs

Ascend C provides high-level APIs for common activations. These compile down to highly optimized vector instructions that process up to 256 bytes per cycle.

### ReLU
```cpp
// Applies ReLU: y = max(x, 0)
Relu(dstLocal, srcLocal, dataSize);
```

### GELU
```cpp
// Applies Gaussian Error Linear Unit
Gelu(dstLocal, srcLocal, dataSize);
```

### Sigmoid
```cpp
// Applies Sigmoid: y = 1 / (1 + exp(-x))
Sigmoid(dstLocal, srcLocal, dataSize);
```

## Performance Optimization

- **Double Buffering**: Since activations are highly memory-bound (low arithmetic intensity), using Double Buffering to overlap MTE transfers with Vector compute is essential.
- **Alignment**: Ensure the `dataSize` processed in a single batch is a multiple of 32 bytes to maximize the 256-bit Vector register utilization and avoid scalar-fallback loops for tail processing.
