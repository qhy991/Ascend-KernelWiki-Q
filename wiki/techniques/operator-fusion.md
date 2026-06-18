---
id: technique-operator-fusion
title: "Operator Fusion"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
confidence: inferred
sources: []
---

# Operator Fusion

Operator Fusion is the practice of combining multiple mathematical operations into a single kernel execution. This minimizes Global Memory (HBM) reads and writes, replacing them with fast on-chip Unified Buffer (UB) or L1 Cache accesses.

## UB Fusion (Unified Buffer Fusion)
UB Fusion is the most common and critical fusion pattern on Ascend. 
If Operator A outputs a tensor that Operator B consumes, and both operate element-wise or point-wise:
1. **Unfused**: A writes to GM -> B reads from GM. (Bandwidth bound).
2. **Fused**: A computes a tile in UB -> B immediately consumes that UB tile -> Writes final result to GM.

### Example: SwiGLU
Instead of separate `matmul`, `silu`, and `mul` kernels:
1. Load $X$ into UB.
2. Compute $X \cdot W_1$ and $X \cdot W_2$ (Cube unit).
3. Apply `SiLU` to the first output (Vector unit, using UB).
4. Multiply by the second output (Vector unit, using UB).
5. Write final $Y$ to GM.

## Graph-Level Fusion (CANN GE)
The CANN Graph Engine (GE) automatically detects common fusion patterns during model compilation (ATC/MindSpore). 
- **Pattern Matching**: GE looks for subgraph patterns (e.g., `Conv2D + BatchNorm + ReLU`) and replaces them with a single fused binary kernel.
- **Custom Fusion**: Developers can register custom fusion passes in the GE to catch proprietary graph structures and route them to a custom AscendC kernel.

## L1 Fusion
For operations involving the Cube Unit (Matmul/Conv), intermediate matrices (like the $QK^T$ matrix in Flash Attention) can be kept resident in the L1 Buffer or L0C. This prevents spilling massive intermediate tensors back to the UB or GM.
