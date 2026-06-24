---
id: kernel-flash-attention-npu
title: "Flash Attention on Ascend NPU"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [attention, flash-attention, cube-unit, softmax]
confidence: inferred
kernel_types: [attention, flash-attention]
languages: [ascendc]
related: [wiki-hardware-cube-unit, hw-vector-unit, technique-cube-vector-overlap, kernel-matmul-ascendc]
sources: [doc-ascendc-api-reference, blog-ascendc-programming-guide]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp16
    shape: "seqlen=4096, headdim=128"
    metric: TFLOPS
    value: 180
    utilization: "~56%"
    source_id: blog-ascendc-programming-guide
reproducibility: concept
techniques: [pipeline-scheduling, cube-vector-overlap, nz-tiling]
---

# Flash Attention Implementation on Ascend NPU

Flash Attention on Ascend NPU implements the standard Flash Attention algorithm—`softmax(Q@K^T) @ V`—but must navigate hardware constraints including NZ format requirements, limited Unified Buffer capacity, and the need to exploit Cube/Vector overlap for performance.

## Algorithm Overview

Flash Attention computes attention in a single pass over sequence length tiles:

```
For each query tile Q[i]:
    Initialize O[i] = 0, l[i] = -inf, m[i] = 0
    For each key/value tile K[j], V[j]:
        S[i,j] = Q[i] @ K[j]^T          (Cube Unit)
        m[i] = max(m[i], max(S[i,j]))   (Vector Unit)
        P[i,j] = exp(S[i,j] - m[i])     (Vector Unit)
        l[i] = sum(P[i,j]) + l[i]       (Vector Unit)
        O[i] = O[i] + P[i,j] @ V[j]     (Cube Unit)
    Output O[i] / l[i]
```

## AscendC Implementation Strategy

### 1. Tiling and Memory Management

```cpp
void FlashAttentionNPU(
    __gm__ half* Q, __gm__ half* K, __gm__ half* V, __gm__ half* Output,
    int seqlen_q, int seqlen_k, int headdim) {
    
    TPipe pipe;
    
    // Q tile stays resident in UB (reused across all K tiles)
    auto Q_tile = AllocUB<half>(TILE_Q * headdim);
    DataCopy(Q_tile, Q, {TILE_Q, headdim});
    
    // Accumulators for online softmax
    auto O_tile = AllocUB<half>(TILE_Q * headdim);
    auto m_vec = AllocUB<half>(TILE_Q);
    auto l_vec = AllocUB<half>(TILE_Q);
    
    // Initialize accumulators
    Fill<half>(O_tile, 0.0, TILE_Q * headdim);
    Fill<half>(m_vec, -INFINITY, TILE_Q);
    Fill<half>(l_vec, 0.0, TILE_Q);
    
    // Stream K and V tiles
    for (int k_tile = 0; k_tile < seqlen_k; k_tile += TILE_KV) {
        // Load K and V tiles (double-buffered)
        auto K_tile = AllocUB<half>(TILE_KV * headdim);
        auto V_tile = AllocUB<half>(TILE_KV * headdim);
        DataCopy(K_tile, K + k_tile * headdim, {TILE_KV, headdim});
        DataCopy(V_tile, V + k_tile * headdim, {TILE_KV, headdim});
        
        // Compute S = Q @ K^T (Cube Unit)
        auto S_tile = AllocUB<half>(TILE_Q * TILE_KV);
        Matmul(S_tile, Q_tile, K_tile, {TILE_Q, TILE_KV, headdim});
        
        // Vector operations: max, exp, sum
        auto new_max = AllocUB<half>(TILE_Q);
        ReduceMax(S_tile, new_max, {TILE_KV}, headdim);
        
        auto m_prev = AllocUB<half>(TILE_Q);
        DataCopy(m_prev, m_vec, TILE_Q);
        
        // m[i] = max(m[i], max(S[i,j]))
        MaxElementwise(m_vec, new_max, m_vec, TILE_Q);
        
        // l[i] = sum(exp(S[i,j] - m[i])) + l[i]
        auto P_tile = AllocUB<half>(TILE_Q * TILE_KV);
        Sub(S_tile, m_vec, S_tile, TILE_Q * TILE_KV);
        Exp(S_tile, P_tile, TILE_Q * TILE_KV);
        
        auto sum_P = AllocUB<half>(TILE_Q);
        ReduceSum(P_tile, sum_P, {TILE_KV}, headdim);
        
        // l[i] = exp(m_prev - m[i]) * l[i] + sum(P)
        auto scale_l = AllocUB<half>(TILE_Q);
        Sub(m_prev, m_vec, scale_l, TILE_Q);
        Exp(scale_l, scale_l, TILE_Q);
        Mul(scale_l, l_vec, l_vec, TILE_Q);
        Add(l_vec, sum_P, l_vec, TILE_Q);
        
        // O[i] = O[i] * exp(m_prev - m[i]) + P @ V
        auto P_V = AllocUB<half>(TILE_Q * headdim);
        Matmul(P_V, P_tile, V_tile, {TILE_Q, headdim, TILE_KV});
        
        auto scaled_O = AllocUB<half>(TILE_Q * headdim);
        Mul(O_tile, scale_l, scaled_O, TILE_Q * headdim);
        Add(O_tile, scaled_O, O_tile, TILE_Q * headdim);
        Add(O_tile, P_V, O_tile, TILE_Q * headdim);
    }
    
    // Final normalization
    auto l_recip = AllocUB<half>(TILE_Q);
    Reciprocal(l_vec, l_recip, TILE_Q);
    Mul(O_tile, l_recip, O_tile, TILE_Q * headdim);
    
    DataCopy(Output, O_tile, {TILE_Q, headdim});
}
```

### 2. Cube/Vector Overlap Strategy

The kernel exploits queue parallelism:

- **Tile k+1**: Cube computes `Q @ K[k+1]^T`
- **Tile k**: Vector computes `max`, `exp`, `sum` on `S[k]`
- **Tile k-1**: Cube computes `P[k-1] @ V[k-1]`

This overlap achieves ~1.4× speedup over serialized execution.

### 3. NZ Format Handling

All matrices (Q, K, V, S, P) must be in NZ format for Cube Unit operations:

- Input Q, K, V: Converted from ND to NZ in prologue
- Intermediate S, P: Automatically produced in NZ format by Matmul
- Output O: Converted from NZ to ND in epilogue

## Challenges and Solutions

**1. Numerical Stability**
- Online softmax requires careful handling of `m_prev` vs `m_curr` differences
- Solution: Scale factor `exp(m_prev - m_curr)` applied to both `O` and `l`

**2. UB Memory Pressure**
- Resident Q tile + streaming K/V tiles + intermediates approach UB capacity
- Solution: Aggressive tile sizing (e.g., TILE_Q=64, TILE_KV=32 for headdim=128)

**3. Reduction Overhead**
- `ReduceMax` and `ReduceSum` on Vector Unit are bandwidth-intensive
- Solution: Fuse max/sum/exp into single pipeline stage where possible

## Performance Comparison

| Platform      | SeqLen | HeadDim | TFLOPS | Utilization | Notes                        |
|---------------|--------|----------|--------|--------------|------------------------------|
| Ascend 910B   | 4096   | 128      | 180    | ~56%         | Cube/Vector overlap enabled  |
| CUDA A100     | 4096   | 128      | 320    | ~73%         | Reference implementation     |
| Ascend 910B   | 2048   | 64       | 165    | ~51%         | Smaller tiles reduce overlap  |

## CUDA vs Ascend Comparison

**CUDA Approach:**
- Shared memory tiling for Q, K, V
- Online softmax with warp-level reductions
- L2 cache for streaming K, V tiles

**Ascend Approach:**
- Unified Buffer replaces shared memory
- Dedicated Vector Unit for reductions
- MTE queues replace memory loaders
- NZ format adds conversion overhead

Key difference: Ascend's strict queue model enables predictable overlap but requires explicit buffer management, whereas CUDA relies on warp synchronization and dynamic shared memory allocation.
