---
id: technique-pr-vllm-ascend-4932
title: "PR Insight: vllm-project/vllm-ascend #4932"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - mtp
  - batch-inference
  - accuracy
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4932"
---

# PR Insight: vllm-project/vllm-ascend #4932

**Title:** [main][BugFix] Fixed an accuracy bug of Qwen3-next-MTP when batched inferring

## Overview
This PR fixes an accuracy bug in Qwen3-Next-MTP when running batched inference. The fix ensures the output matches GPU/NPU reference and eliminates redundant tokens. The patch is applied to the worker module patch system.

## Technical Significance
Resolves batch inference correctness issues in Qwen3-Next MTP speculative decoding. Ensures deterministic output when multiple prompts are processed together in a batch, which is critical for production inference serving.

## Related
- `kernel-qwen3-next`
- `technique-mtp`
- `technique-batch-inference`
- `technique-speculative-decoding`