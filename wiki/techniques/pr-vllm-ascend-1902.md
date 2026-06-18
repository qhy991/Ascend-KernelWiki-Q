---
id: technique-pr-vllm-ascend-1902
title: "PR Insight: vllm-project/vllm-ascend #1902"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gating
  - fused-ops
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1902"
---

# PR Insight: vllm-project/vllm-ascend #1902

**Title:** [0.9.1][Perf] apply npu_moe_gating_top_k_softmax for moe

## Overview
This PR applies the npu_moe_gating_top_k_softmax fused operation for MoE gating computation. The operation combines top-k selection and softmax into a single kernel, improving performance for MoE expert routing.

## Technical Significance
Operator fusion for MoE gating. The MoE gating operation involves selecting top-k experts and computing softmax weights, which are fused into a single NPU operation to reduce kernel launch overhead and improve data locality.

## Related
- `kernel-moe-ascendc`
- `technique-operator-fusion`
- `technique-moe-gating`