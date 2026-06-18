---
id: technique-pr-vllm-ascend-1335
title: "PR Insight: vllm-project/vllm-ascend #1335"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - allgather
  - expert-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1335"
---

# PR Insight: vllm-project/vllm-ascend #1335

**Title:** support fused_moe_allgather_ep

## Overview
This PR adds support for fused MoE all-gather in expert parallel (EP) mode, optimizing communication during distributed MoE inference.

## Technical Significance
Improves MoE inference performance by fusing all-gather operations for expert weights and activations, reducing communication overhead in expert parallel deployments. The implementation adds new test coverage and updates fused MoE operator to support EP all-gather patterns, which is essential for large-scale distributed MoE inference.

## Related
- `kernel-moe`
- `technique-hccl-optimization`
- `technique-operator-fusion`