import os

wiki_kernels_path = "/Users/haiyan-mini/Agent4Kernel/ascend-kernelwiki-q/wiki/kernels"
wiki_patterns_path = "/Users/haiyan-mini/Agent4Kernel/ascend-kernelwiki-q/wiki/patterns"

rope_content = """---
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
"""

swiglu_content = """---
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
"""

tque_deadlock_content = """---
id: wiki-pattern-tque-deadlock
title: TQue Deadlock Pattern in Ascend C
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [instruction-queue, pipeline-scheduling, ascendc]
confidence: verified
sources: [doc-ascendc-api-reference]
---

# TQue Deadlock

Queue deadlocks are one of the most common issues when writing Ascend C pipeline kernels. They occur when the pipeline stalls permanently due to an improper sequence of `AllocTensor`, `EnQue`, `DeQue`, and `FreeTensor`.

## Symptoms

- Kernel hangs indefinitely.
- `msprof` shows no computation after a certain point.
- Only a few tiles process before execution completely stops.

## Common Causes

### 1. Missing FreeTensor
If a `LocalTensor` is `DeQue`'d but never returned to the pool using `FreeTensor`, the pool of available buffers is exhausted.

```cpp
// BAD
LocalTensor<half> xLocal = inQueue.DeQue<half>();
// ... compute ...
// Missing: inQueue.FreeTensor(xLocal);

// GOOD
LocalTensor<half> xLocal = inQueue.DeQue<half>();
// ... compute ...
inQueue.FreeTensor(xLocal); 
```

### 2. Mismatched Alloc/EnQue
Calling `AllocTensor` but forgetting to `EnQue` means the downstream component will hang indefinitely on its `DeQue` call.

```cpp
// BAD
LocalTensor<half> xLocal = outQueue.AllocTensor<half>();
// ... write data ...
// Missing: outQueue.EnQue(xLocal);
```

### 3. Loop Iteration Count Mismatch
If the producer (`CopyIn`) loops `N` times but the consumer (`Compute`) loops `M` times, one will wait on a queue forever.

## Solution and Best Practices

- Always ensure that for every `AllocTensor`, there is a corresponding `EnQue` or `FreeTensor`.
- Always ensure that for every `DeQue`, there is a corresponding `FreeTensor` or `EnQue`.
- Keep loop boundaries synchronized between pipeline stages.
- When branching, ensure tensors are freed or enqueued along all control paths.
"""

os.makedirs(wiki_kernels_path, exist_ok=True)
os.makedirs(wiki_patterns_path, exist_ok=True)

with open(os.path.join(wiki_kernels_path, "rope-ascendc.md"), "w") as f:
    f.write(rope_content)

with open(os.path.join(wiki_kernels_path, "swiglu-ascendc.md"), "w") as f:
    f.write(swiglu_content)

with open(os.path.join(wiki_patterns_path, "tque-deadlock.md"), "w") as f:
    f.write(tque_deadlock_content)

print("Ascend-KernelWiki-Q generation script complete.")
