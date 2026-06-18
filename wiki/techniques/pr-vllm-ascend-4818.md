---
id: technique-pr-vllm-ascend-4818
title: "PR Insight: vllm-project/vllm-ascend #4818"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - qwen3-next
  - gateddeltanet
  - sigmoid-gating
  - delta-rule-update
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4818"
---

# PR Insight: vllm-project/vllm-ascend #4818

**Title:** [pref] qwen3_next add triton ops : fused_sigmoid_gating_delta_rule_update

## Overview
This PR adds a fused Triton operator `fused_sigmoid_gating_delta_rule_update` for Qwen3-Next, combining `fused_gdn_gating` and `fused_recurrent_gated_delta_rule` operations into a single kernel. The fusion reduces graph complexity from multiple operations to one fused operation.

## Technical Significance
Fuses two critical operations in Qwen3-Next's GatedDeltaNet architecture: sigmoid gating and recurrent gated delta rule update. This reduces kernel launch overhead and improves memory access patterns, enhancing overall inference performance.

## Related
- `kernel-fused-sigmoid-gating-delta-rule-update`
- `kernel-fused-gdn-gating`
- `kernel-recurrent-gated-delta-rule`
- `kernel-qwen3-next`
- `kernel-gateddeltanet`
- `technique-operator-fusion`