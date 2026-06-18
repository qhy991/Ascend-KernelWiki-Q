---
id: technique-pr-vllm-ascend-6009
title: "PR Insight: vllm-project/vllm-ascend #6009"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - mrope
  - revert
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6009"
---

# PR Insight: vllm-project/vllm-ascend #6009

**Title:** [0.13.0][cherry-pick][bugfix] fix bug of triton mrope

## Overview
This is a cherry-pick of PR #5827 for the v0.13.0 release branch, which was later reverted. It attempted to fix bugs in the Triton mrope implementation for Qwen3-VL models.

## Technical Significance
This PR was part of an effort to bring Triton mrope optimizations to the v0.13.0 branch. However, issues were discovered, leading to its subsequent reversion. The existence of this PR and its reversion highlights the complexity of integrating Triton kernels with multimodal models and the importance of thorough testing across different model configurations.

## Related
- `technique-triton`, `technique-mrope`, `technique-revert`