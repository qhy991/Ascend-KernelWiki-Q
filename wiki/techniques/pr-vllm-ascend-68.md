---
id: technique-pr-vllm-ascend-68
title: "PR Insight: vllm-project/vllm-ascend #68"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - operator-fusion
  - ascendc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/68"
---

# PR Insight: vllm-project/vllm-ascend #68

**Title:** [Hardware][Ascend]forward_oot for FusedMoE

## Overview
This PR implements the Ascend-specific forward_oot method for FusedMoE, including NPU versions of group_topk and fused_expert functions. The new ops/fused_moe.py file (170 lines) adds MoE support for DeepSeek models on Ascend hardware.

## Technical Significance
Mixture of Experts is critical for large-scale models like DeepSeek. This implementation provides Ascend-optimized kernels for the hot MoE path: expert routing (group_topk) and expert computation (fused_expert). The forward_oot pattern allows custom kernels to override default implementations.

## Related
- kernel-moe
- technique-operator-fusion