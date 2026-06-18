---
id: technique-pr-vllm-ascend-7000
title: "PR Insight: vllm-project/vllm-ascend #7000"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - h2d
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7000"
---

# PR Insight: vllm-project/vllm-ascend #7000

**Title:** [MOE][Bugfix] Cancel H2D for expert_map

## Overview
Fixes a bug where repeated answers occur in long output scenarios when `expert_map` is on device. The fix cancels host-to-device (H2D) transfers for `expert_map` to prevent synchronization issues.

## Technical Significance
Prevents output corruption in long generation scenarios for MoE models by eliminating unnecessary H2D transfers that cause synchronization problems. The fix ensures correct expert routing and prevents repeated or garbled output.

## Related
- `technique-moe`, `technique-expert-routing`, `technique-h2d-optimization`