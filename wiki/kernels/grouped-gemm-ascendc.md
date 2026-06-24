---
id: kernel-grouped-gemm-ascendc
title: "Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [grouped-gemm, gemm, matmul, moe, batch]
confidence: inferred
kernel_types: [grouped-gemm, gemm]
languages: [ascendc]
related: [kernel-matmul-ascendc, kernel-moe-ascendc, wiki-hardware-cube-unit]
sources: [doc-ascendc-api-reference, doc-catlass-framework]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp16
    shape: "groups=8, M=512, N=4096, K=4096"
    metric: TFLOPS
    value: 160
    utilization: "~50%"
    source_id: doc-catlass-framework
reproducibility: concept
techniques: [pipeline-scheduling, nz-tiling, cube-vector-overlap]
---

# Grouped GEMM on Ascend NPU

Grouped GEMM executes multiple independent GEMM operations with different M dimensions per group in a single kernel launch. This pattern is critical for modern workloads like Mixture-of-Experts (MoE) models (per-expert matrix multiplication) and Grouped Query Attention (GQA), where different experts or attention heads require different batch sizes.

## Implementation on Ascend

On Ascend NPUs, each group gets its own Cube matmul operation with NZ format data. Three primary implementation approaches:

1. **Sequential Execution**: Loop over groups, executing one Matmul per iteration
2. **Multi-core Parallel**: Assign different groups to different AICores
3. **Fused Template**: Use Catlass grouped-GEMM template with automatic scheduling

## Key Challenge: Load Imbalance

When groups have highly variable M dimensions, static scheduling leads to severe load imbalance. For example, in MoE routing, expert activation patterns follow a power law — some experts receive 10-100× more tokens than others.

## AscendC Implementation Pattern

```ascendc
// Pseudo-code for grouped GEMM
for (int g = 0; g < num_groups; g++) {
    // Load group-specific matrices in NZ format
    DataCopy(inputs[g], NZ_buffer_A[g], M[g] * K);
    DataCopy(weights[g], NZ_buffer_B[g], K * N);
    
    // Cube matmul for this group
    Matmul(NZ_buffer_A[g], NZ_buffer_B[g], output[g], M[g], N, K);
    
    // Vector epilogue: bias, activation, store
    PipeBarrier();
}
```

## Performance Considerations

- **Memory overhead**: NZ format padding increases memory footprint by ~6%
- **Scheduling**: Dynamic work distribution improves utilization for imbalanced groups
- **Comparison with CUDA**: CUTLASS grouped-GEMM uses threadblock-level scheduling; Catlass groups at AICore granularity

## Use Cases

- **MoE Experts**: Each expert = one GEMM group with dynamic M (batch size per expert)
- **Grouped Query Attention**: Separate GEMMs for key/value projections per attention head group
- **Batched inference**: Different sequence lengths in same batch

## Related Patterns

- [MatMul on Ascend](kernel-matmul-ascendc) — single-group GEMM foundation
- [MoE Kernels](kernel-moe-ascendc) — expert routing + dispatch patterns
- [Pipeline Scheduling](technique-pipeline-scheduling) — overlapping groups with double buffering
