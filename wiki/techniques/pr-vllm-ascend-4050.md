---
id: technique-pr-vllm-ascend-4050
title: "PR Insight: vllm-project/vllm-ascend #4050"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gating-topk
  - generalization
  - quantization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4050"
---

# PR Insight: vllm-project/vllm-ascend #4050

**Title:** [refactor]support gatingtopk operator generalization

## Overview
This PR generalizes the `npu_moe_gating_top_k` operator to support all group_count sizes, removing the previous limitation of only supporting 'group_count=256' pattern. The functionality of `torch_npu.npu_moe_gating_top_k_softmax` is included in the generalized `torch_npu.npu_moe_gating_top_k`. The changes depend on CANN 8.3.RC1 and provide 6% TPS improvement for GLM4.5-w8a8.

## Technical Significance
Generalizing the gating operator removes artificial constraints on MoE model configurations, supporting a wider range of models. The TPS improvement for GLM4.5-w8a8 demonstrates the performance benefits of the generalized operator. Removing the group_count limitation enables better hardware utilization for MoE models with different expert group configurations on Ascend NPUs.

## Related
- `technique-moe`, `technique-gating`, `pattern-operator-generalization`, `technique-performance-optimization`