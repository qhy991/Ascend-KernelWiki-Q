---
id: technique-pr-vllm-ascend-3381
title: "PR Insight: vllm-project/vllm-ascend #3381"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3381"
---

# PR Insight: vllm-project/vllm-ascend #3381

**Title:** [BugFix]Fix moe load problems in torchair when using dynamic eplb

## Overview
When using dynamic eplb, moe load is not imported. We fix this problem by modifying the return value of hidden states in torchair.

## Technical Significance
Fixes MoE loading problems in TorchAir environment when using dynamic EPLB for expert routing.

## Related
- `technique-moe-routing`
- `technique-kv-cache-paging`
