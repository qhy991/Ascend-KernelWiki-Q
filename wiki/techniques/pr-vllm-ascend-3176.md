---
id: technique-pr-vllm-ascend-3176
title: "PR Insight: vllm-project/vllm-ascend #3176"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - refactoring
  - code-cleanup
  - qwen3-moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3176"
---

# PR Insight: vllm-project/vllm-ascend #3176

**Title:** [MoE] [Refactor] Combine common_fused_moe and fused_moe

## Overview
This PR consolidates common_fused_moe and fused_moe by moving additional functionality from fused_moe.py to common_fused_moe.py and removing fused_moe.py. It also removes unnecessary custom classes from qwen3_moe.py, which will be completely removed after vllm-ascend v0.11.0.

## Technical Significance
Code consolidation reduces duplication and maintenance burden. Merging the MoE implementations ensures consistent behavior across different usage patterns and makes it easier to add optimizations. Removing temporary workarounds simplifies the codebase as the platform matures.

## Related
- `kernel-moe-ascendc`, `pattern-code-refactoring`, `kernel-qwen3-moe-ascendc`