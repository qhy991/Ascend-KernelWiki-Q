---
id: technique-pr-vllm-ascend-6444
title: "PR Insight: vllm-project/vllm-ascend #6444"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - rope
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6444"
---

# PR Insight: vllm-project/vllm-ascend #6444

**Title:** [0.13.0][cherry-pick]pick from 6310 to fix rope op

## Overview
This is a cherry-pick from PR #6310 to fix a rotary embedding (RoPE) operator error specifically for GLM models. The fix is applied to the 0.13.0 release branch.

## Technical Significance
Fixes a RoPE operator bug affecting GLM model inference. The fix ensures correct rotary embedding operations which are critical for positional encoding in transformer models, preventing incorrect attention calculations that would cause accuracy issues.

## Related
- `kernel-attention`