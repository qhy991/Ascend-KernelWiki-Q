---
id: technique-pr-vllm-ascend-10016
title: "PR Insight: vllm-project/vllm-ascend #10016"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - sigmoid
  - gating
  - delta-rule
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10016"
---

# PR Insight: vllm-project/vllm-ascend #10016

**Title:** [Misc][Ops] Fix a bug inside a triton operator fused_sigmoid_gating_delta_rule_update_kernel

## Overview
This PR fixes a bug in the fused_sigmoid_gating_delta_rule_update_kernel Triton operator, which combines sigmoid, gating, and delta rule update operations into a single kernel.

## Technical Significance
Fixes correctness issues in the fused sigmoid, gating, and delta rule update kernel. Ensures that this complex fused operation produces correct results, which is critical for models using delta rule updates with sigmoid gating.

## Related
- `kernel-triton`, `kernel-sigmoid`, `technique-operator-fusion`