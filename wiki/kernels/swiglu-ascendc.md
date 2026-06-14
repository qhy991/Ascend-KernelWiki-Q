---
id: wiki-kernel-swiglu-ascendc
title: SwiGLU Activation Implementation in Ascend C
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [vector-unit, ascendc, elementwise, math]
confidence: verified
kernel_types: [elementwise, math]
languages: [ascendc]
sources: [doc-ascendc-api-reference]
reproducibility: pseudocode
---

# SwiGLU Activation

SwiGLU (Swish-Gated Linear Unit) is widely used in the Feed-Forward Networks of recent LLMs like LLaMA and PaLM.

## Formula

`SwiGLU(x, W, V) = Swish(xW) ⊙ (xV)`
Where `Swish(x) = x * Sigmoid(beta * x)`.

Usually, the Matrix Multiplications (`xW` and `xV`) are handled by Cube unit (GEMM kernels), and the Swish + Element-wise multiplication is done as a fused activation or a standalone element-wise kernel.

## Ascend C Implementation

This focuses on the Element-wise portion (Vector Unit).

### Pseudocode

```cpp
// inputs: gate_tensor (xW), up_tensor (xV)
// output: out_tensor

// 1. Swish(gate_tensor) = gate_tensor * Sigmoid(gate_tensor)
LocalTensor<half> sigmoid_out = tempQueue.AllocTensor<half>();
Sigmoid(sigmoid_out, gate_tensor, count);
Mul(gate_tensor, gate_tensor, sigmoid_out, count); // gate_tensor now holds Swish output

// 2. Swish(gate_tensor) ⊙ up_tensor
Mul(out_tensor, gate_tensor, up_tensor, count);
```

## Optimizations
- Combine the SwiGLU operation directly into the epilogue of the preceding GEMM (if using custom Cube kernels) to save global memory roundtrips (Data Reuse).
- Utilize double buffering for the `gate_tensor` and `up_tensor` if written as a standalone kernel.
