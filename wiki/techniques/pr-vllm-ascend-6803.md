---
id: technique-pr-vllm-ascend-6803
title: "PR Insight: vllm-project/vllm-ascend #6803"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - attention
  - accuracy
  - bugfix
  - 310p
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6803"
---

# PR Insight: vllm-project/vllm-ascend #6803

**Title:** [BugFix] [310p] Fix attention accuracy issue

## Overview
This PR fixes attention accuracy issues on 310P by enhancing AttentionMaskBuilder310 to correctly handle maximum model length based on model configuration rather than fixed internal values. It also updates fused_moe implementation to the main branch.

## Technical Significance
Ensures correct attention mask generation for 310P devices, which is critical for attention mechanism correctness. The configuration-based approach prevents hardcoding issues and ensures accuracy across different model configurations.

## Related
- `kernel-attention`