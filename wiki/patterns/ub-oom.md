---
id: pattern-ub-oom
title: "UB OOM (Unified Buffer Overflow)"
type: wiki-pattern
architectures:
  - ascend910
  - ascend910b
tags:
  - debugging
  - memory
confidence: inferred
sources: []
---

# UB OOM (Unified Buffer Overflow)

The Unified Buffer (UB) is the primary software-managed scratchpad memory on the Ascend AI Core (similar to Shared Memory on a GPU). It has a strict size limit (e.g., 256KB on 910A, larger on 910B). Exceeding this limit causes an immediate compilation failure or runtime memory corruption.

## Symptoms
- **Compile Time**: `TQue` allocation failures or compiler errors stating `workspace exceeds UB size`.
- **Runtime**: Silent data corruption or hardware traps (Memory Violation) if raw pointers are abused outside the `TQue` API.

## Diagnosis and Solutions

### 1. Overly Aggressive Pipeline Depth
A Ping-Pong buffer (depth 2) requires `2 * TileSize`. A Triple buffer requires `3 * TileSize`. If you allocate multi-stage queues for `VECIN`, `VECOUT`, and intermediate calculations, the total memory quickly explodes.
- **Fix**: Reduce the `TQue` depth. If a depth of 2 causes UB OOM, fall back to a single buffer (depth 1) and sacrifice some DMA overlap.

### 2. Sub-optimal Tiling Size
The tile size dictates how large each block in the UB is. 
- **Fix**: Reduce the `blockDim` data size. For example, instead of loading a tile of 4096 elements, load 1024 elements and execute the inner loop 4 times.

### 3. Memory Re-use (In-place Operations)
If a Vector operation reads $A$ and writes $B$, and $A$ is never used again, allocating separate UB tensors for $A$ and $B$ wastes space.
- **Fix**: Use in-place operations. Many AscendC Vector APIs allow the source and destination `LocalTensor` to be the same memory address.
```cpp
// In-place Exp
Exp(tensor_A, tensor_A, size);
```

### 4. Dynamic UB Allocation
Avoid defining large static arrays. Always use the `TPipe` and `TQue` dynamic memory management system. Use `FreeTensor` to immediately release memory back to the UB pool as soon as the data is consumed by the DMA out engine.

## Real-World Context: torch_npu & Triton

When executing models in PyTorch via the `torch_npu` backend, UB OOM errors frequently surface during complex operations:
- **Fused Operators**: Deeply fused operations (like `fused_linear` or MoE routing kernels) may demand larger UB space than standard ops. If you hit an OOM, falling back to unfused PyTorch primitives or reducing batch/sequence length can confirm if peak UB pressure is the culprit.
- **Triton Kernels on Ascend**: If writing custom Triton kernels targeting the Ascend backend, ensure your block sizes (`BLOCK_M`, `BLOCK_N`) do not force the compiler to over-allocate the UB. Shrinking the Triton block sizes directly reduces UB consumption.
