---
id: technique-pr-vllm-ascend-1547
title: "PR Insight: vllm-project/vllm-ascend #1547"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - alltoallv
  - dpo
  - communication
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1547"
---

# PR Insight: vllm-project/vllm-ascend #1547

**Title:** [0.9.1][Feature]Moe alltoallv communication optimization for unquantized RL training sence & alltoallv support dpo

## Overview
This PR optimizes MoE alltoallv communication for unquantized RL training scenarios and adds DPO (Direct Preference Optimization) support.

## Technical Significance
Improves MoE training performance by optimizing alltoallv communication patterns, reducing synchronization overhead during expert parallel training. The addition of DPO support enables preference optimization workflows, expanding training capabilities beyond standard supervised fine-tuning.

## Related
- `kernel-moe`
- `technique-hccl-optimization`
- `technique-dpo`