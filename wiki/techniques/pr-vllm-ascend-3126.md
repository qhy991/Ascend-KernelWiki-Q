---
id: technique-pr-vllm-ascend-3126
title: "PR Insight: vllm-project/vllm-ascend #3126"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - mc2
  - operator-elimination
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3126"
---

# PR Insight: vllm-project/vllm-ascend #3126

**Title:** Remove qwen3 moe MC2 cumsum & cast

## Overview
This PR eliminates redundant cumsum and cast operators in Qwen3 MoE MC2 graph execution. After npu_moe_distribute_dispatch_v2, these operations become unnecessary when using expert_token_nums_type=0 and not converting weight_scale to float32.

## Technical Significance
Operator elimination reduces computational overhead and improves inference performance. The MC2 (MoE Communication 2) graph optimization removes redundant data transformations that were previously required but are now handled by improved Ascend operators, demonstrating continuous operator evolution.

## Related
- `kernel-moe-ascendc`, `technique-operator-fusion`, `kernel-qwen3-moe-ascendc`