---
id: technique-pr-vllm-ascend-9413
title: "PR Insight: vllm-project/vllm-ascend #9413"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - shared-expert
  - overlap
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9413"
---

# PR Insight: vllm-project/vllm-ascend #9413

**Title:** [Performance] Optimize shared expert overlap timing in FusedMoE

## Overview
This PR optimizes the timing of shared expert overlap in the FusedMoE implementation. The changes affect the forward context, DeepSeek V4 model code, fused MoE operator, and linear operations to improve compute-communication overlap efficiency.

## Technical Significance
Proper overlap timing is critical for maximizing the benefits of compute-communication parallelism. Optimizing shared expert overlap reduces idle time and improves overall MoE inference throughput, which is particularly important for models with many experts.

## Related
- `kernel-moe`
- `technique-cube-vector-overlap`