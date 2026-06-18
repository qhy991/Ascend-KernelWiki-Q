---
id: technique-pr-vllm-ascend-4811
title: "PR Insight: vllm-project/vllm-ascend #4811"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen2.5-vl
  - mrope
  - precision
  - bugfix
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4811"
---

# PR Insight: vllm-project/vllm-ascend #4811

**Title:** [cherry-pick]fix qwen3vl mrope op (#4484)

## Overview
This PR cherry-picks a fix for Qwen2.5-VL mrope (multimodal rotary position embedding) precision problems from PR #4484. The fix is applied to vllm_ascend/ops/rotary_embedding.py.

## Technical Significance
Resolves precision issues in multimodal rotary position embedding for Qwen2.5-VL vision-language models. The fix improves accuracy on vision-language tasks like textVQA when running on Ascend hardware.

## Related
- `kernel-rotary-embedding`
- `technique-mrope`
- `kernel-qwen2.5-vl`
- `technique-vl-models`