---
id: technique-pr-vllm-ascend-9423
title: "PR Insight: vllm-project/vllm-ascend #9423"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - moe-gating
  - bugfix
  - ub
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9423"
---

# PR Insight: vllm-project/vllm-ascend #9423

**Title:** [BugFix][Model] Fix moe_gating_topk_hash UB out of bounds in dummy load for DeepSeek V4

## Overview
This PR fixes a unified buffer (UB) out-of-bounds error in the moe_gating_topk_hash operation during dummy load for DeepSeek V4. The fix is implemented in the DeepSeek V4 model code to ensure proper memory access bounds.

## Technical Significance
UB out-of-bounds errors can cause crashes, data corruption, or undefined behavior. Fixing this issue ensures reliable and correct expert routing for DeepSeek V4 models, particularly during initialization and dummy load phases.

## Related
- `kernel-moe`
- `hw-unified-buffer`