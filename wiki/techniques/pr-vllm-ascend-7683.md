---
id: technique-pr-vllm-ascend-7683
title: "PR Insight: vllm-project/vllm-ascend #7683"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - flash-comm
  - qwen3.5
  - mtp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7683"
---

# PR Insight: vllm-project/vllm-ascend #7683

**Title:** [BugFix] Fix Qwen3.5 MoE flash comm v1 shared expert shape error of mtp layer on A2

## Overview
This PR fixes a shared expert shape error in Qwen3.5 MoE flash communication v1 for the MTP layer on Ascend 910B (A2). The fix affects custom operator registration and Eagle proposer.

## Technical Significance
Resolves shape mismatch issues in Qwen3.5 MoE models during multi-token prediction, ensuring correct tensor shapes for shared expert processing in flash communication patterns.

## Related
- `kernel-moe`, `technique-flash-communication`, `pattern-qwen-architecture`, `technique-speculative-decoding`, `pattern-moe-routing`