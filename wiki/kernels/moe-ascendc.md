---
id: kernel-moe-ascendc
title: "MoE (Mixture of Experts) Kernel on Ascend NPU"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [moe, grouped-gemm, routing, ascendc]
confidence: inferred
kernel_types: [moe, grouped-gemm]
languages: [ascendc]
related: [kernel-matmul-ascendc, hw-cube-unit, technique-pipeline-scheduling]
sources: [doc-ascendc-api-reference, doc-catlass-framework]
performance_claims:
  - gpu: Ascend 910B
    dtype: fp16
    shape: "tokens=4096, experts=8, hidden=4096"
    metric: TFLOPS
    value: 180
    utilization: "~56%"
    source_id: doc-catlass-framework
reproducibility: concept
techniques: [pipeline-scheduling, data-reuse]
---

# MoE (Mixture of Experts) Kernel on Ascend NPU

## Overview

MoE (Mixture of Experts) is a key architectural component in modern large language models like DeepSeek-MoE, Mixtral, and others. The core computation consists of two stages: routing and grouped GEMM. During routing, a gate network selects the top-k experts for each token based on learned weights. During grouped GEMM, each token is processed only by its selected experts, enabling model scaling without proportional computational cost increase.

## Implementation on Ascend NPU

The Ascend NPU implementation of MoE kernels leverages the heterogenous computing architecture with specialized units:

**Stage 1: Gate Computation (Vector Unit)**
- Softmax computation on gate logits for all experts
- Top-k selection to identify which experts process each token
- Generation of routing indices and scaling factors

**Stage 2: Token Routing (Scatter/Gather)**
- Token distribution to expert-specific buffers using scatter operations
- Load balancing to prevent expert congestion
- Formation of expert batches for efficient matrix multiplication

**Stage 3: Expert GEMM (Cube Unit)**
- Per-expert matrix multiplication using the Cube unit
- NZ format conversion for optimal Cube unit utilization
- Parallel processing across multiple AICores

**Stage 4: Result Aggregation (Vector Unit)**
- Weighted sum of expert outputs using gating weights
- Result combination via gather operations
- Final output generation

## AscendC Kernel Structure

The AscendC implementation follows a multi-kernel pattern:

```ascendc
// Router Kernel: Compute gate probabilities and routing
extern "C" __global__ void RouterKernel(
    __gm____half__* gate_logits,      // [tokens, experts]
    __gm____int32__* routing_indices, // [tokens, topk]
    __gm____half__* routing_weights   // [tokens, topk]
) {
    // Vector unit softmax + topk
    // Generate routing metadata
}

// Expert GEMM Kernel: Process tokens for each expert
extern "C" __global__ void ExpertGEMMKernel(
    __gm____half__* expert_weights,   // [experts, hidden, ffn_hidden]
    __gm____half__* expert_inputs,    // Tokens routed to this expert
    __gm____half__* expert_outputs    // Expert outputs
) {
    // Cube unit GEMM with NZ format
    // Batch processing for load balancing
}

// Combine Kernel: Aggregate expert outputs
extern "C" __global__ void CombineKernel(
    __gm____half__* expert_outputs,   // [experts, tokens, ffn_hidden]
    __gm____int32__* routing_indices,
    __gm____half__* routing_weights,
    __gm____half__* final_output      // [tokens, ffn_hidden]
) {
    // Vector unit weighted sum
    // Gather-based aggregation
}
```

## Key Challenges and Optimizations

**Load Imbalance**: The distribution of tokens across experts is often non-uniform, leading to some experts becoming bottlenecks. The Ascend implementation addresses this through:
- Dynamic batch sizing per expert
- Work stealing between AICores
- Adaptive routing strategies

**Memory Optimization**: 
- Expert weight caching in L1/L2 buffers
- Token buffer reuse across routing stages
- In-place operations where possible

**Compute Efficiency**:
- NZ format optimization for Cube unit GEMM
- Pipeline scheduling to hide memory latency
- Multi-expert parallel processing

## Performance Characteristics

On Ascend 910B with fp16 precision:
- MoE routing overhead: ~5-10% of total compute time
- Per-expert GEMM throughput: 180 TFLOPS (~56% theoretical peak)
- Scalability: Performance scales linearly with expert count up to hardware limits

## Comparison with GPU Implementation

Compared to DeepSeek-MoE on GPU:
- **Advantages**: Higher throughput for large expert counts, better load balancing with dynamic scheduling
- **Trade-offs**: More complex kernel structure, requires explicit NZ format management
- **Convergence**: Both architectures face similar load balancing and memory bandwidth challenges

The Ascend MoE implementation demonstrates how heterogenous compute units can be orchestrated efficiently for complex, dynamic computational patterns like mixture of experts.