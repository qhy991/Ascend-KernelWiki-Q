---
id: doc-ascend-operator-fusion
title: "Operator Fusion Patterns on Ascend NPU"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [fusion, operator, optimization, cann]
date: '2026-02-15'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0065.html
hardware_features: [cube-unit, vector-unit, unified-buffer]
techniques: [data-reuse, pipeline-scheduling, cube-vector-overlap]
confidence: verified
---

# Ascend Operator Fusion Patterns

CANN framework documentation for operator fusion techniques to reduce memory traffic and maximize AICore utilization.

## Common Fusion Patterns

### 1. MatMul + BiasAdd + Activation

Fuse epilogue operations into single kernel:
```ascendc
// Fused: MatMul → BiasAdd → GELU → Store
Process() {
    Matmul(A_ub, B_ub, C_ub, M, N, K);
    Add(C_ub, bias_ub, C_ub, M*N);
    GELU(C_ub, C_ub, M*N);
    DataCopy(C_gm, C_ub, M*N);
}
```

**Benefit**: Eliminates 2 round-trips to Global Memory

### 2. LayerNorm + Residual + Dropout

Single-pass Vector pipeline:
```ascendc
// Fused normalization pipeline
Process() {
    // Residual add
    Add(input_ub, residual_ub, output_ub, size);
    
    // LayerNorm in-place (mean, variance computed once)
    LayerNorm(output_ub, gamma, beta, output_ub, size);
    
    // Dropout (apply mask during LN)
    Dropout(output_ub, mask_ub, output_ub, size, rate);
}
```

**Benefit**: Keeps all activations in UB, avoids GM store/load

### 3. Attention Fusion

QKV projection → score → softmax → dropout → V projection:
```ascendc
// All attention stages in one kernel
Process() {
    // QKV projection (3 grouped GEMMs)
    GroupedGEMM(input_ub, qkv_weights_ub, qkv_ub, ...);
    
    // Score computation (QK^T / sqrt(d_k))
    Matmul(q_ub, k_ub_T, score_ub, ...);
    Scale(score_ub, scale_factor);
    
    // Softmax
    Softmax(score_ub, attn_ub, ...);
    
    // Dropout
    Dropout(attn_ub, mask_ub, attn_ub, ...);
    
    // V projection (attn @ V)
    Matmul(attn_ub, v_ub, output_ub, ...);
}
```

**Benefit**: Eliminates 5 intermediate GM stores

### 4. GELU + MatMul

Fuse activation into GEMM epilogue:
```ascendc
// Activation as part of GEMM post-processing
Matmul(A_ub, B_ub, C_ub, M, N, K, 
       epilogue={bias_add, gelu_activation});
```

**Benefit**: Reduces Vector queue operations

## Performance Benefits

**Memory Reduction**: Typical fusion reduces GM traffic by 40-60%

**Latency Improvement**: 
- MatMul+Activation: 15-20% faster
- Attention fusion: 30-40% faster
- LayerNorm pipeline: 25% faster

## Implementation Guidelines

1. **Identify producer-consumer chains**: Fuse when output of one op is only consumed by next op
2. **UB budget management**: Ensure all intermediate results fit in UB
3. **Queue placement**: Assign ops to appropriate queue (Vector vs Cube) for maximum overlap
4. **Granularity**: Fuse at kernel level (multiple ops in one `Process` call), not across kernel boundaries

## Tools and APIs

- AscendC fusion templates with `TPE` (Tensor Processing Engine) API
- AscendCL automatic operator fusion (compiler-based)
- MindSpore automatic fusion with `@fuse` decorator

## Related Patterns

- [Pipeline Scheduling](technique-pipeline-scheduling) — queue overlap in fused kernels
- [Data Reuse](technique-data-reuse) — UB cache management
- [Cube-Vector Overlap](technique-cube-vector-overlap) — concurrent execution in fused pipelines
