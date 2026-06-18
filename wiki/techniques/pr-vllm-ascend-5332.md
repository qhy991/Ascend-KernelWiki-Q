---
id: technique-pr-vllm-ascend-5332
title: "PR Insight: vllm-project/vllm-ascend #5332"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - aclnn
  - custom-operator
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5332"
---

# PR Insight: vllm-project/vllm-ascend #5332

**Title:** [OP] Enable custom op aclnnMoeInitRoutingCustom

## Overview
This PR enables the custom operator `aclnnMoeInitRoutingCustom` that was introduced in PR #5251, making it available for use in vLLM-Ascend MoE workloads.

## Technical Significance
Enabling the custom MoE routing operator provides access to optimized expert routing functionality on Ascend NPUs. The operator supports various quantization scenarios and provides performance benefits for MoE inference by replacing community implementations with Ascend-optimized kernels.

## Related
- technique-moe
- technique-custom-operators
- technique-expert-routing