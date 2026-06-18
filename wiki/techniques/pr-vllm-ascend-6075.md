---
id: technique-pr-vllm-ascend-6075
title: "PR Insight: vllm-project/vllm-ascend #6075"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - mrope
  - revert
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6075"
---

# PR Insight: vllm-project/vllm-ascend #6075

**Title:** Revert "[0.13.0][cherry-pick][bugfix] fix bug of triton mrope"

## Overview
This PR reverts PR #6009, which was a cherry-pick of the Triton mrope fix. The revert indicates that the fix introduced issues in the v0.13.0 branch, requiring it to be rolled back.

## Technical Significance
Reverts are an important part of maintaining release branch stability. The existence of this revert suggests that the Triton mrope fix from PR #5827 had compatibility issues when backported to v0.13.0. This highlights the importance of thorough testing for cherry-picks and the need to be cautious about bringing optimizations to release branches.

## Related
- `technique-triton`, `technique-mrope`, `technique-revert`