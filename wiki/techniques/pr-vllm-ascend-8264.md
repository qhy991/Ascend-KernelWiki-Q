---
id: technique-pr-vllm-ascend-8264
title: "PR Insight: vllm-project/vllm-ascend #8264"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - bugfix
  - short-prompt
  - mla
  - prefill
  - decode
  - state-management
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8264"
---

# PR Insight: vllm-project/vllm-ascend #8264

**Title:** [0.18.0][BugFix] Add PrefillNoCache state in mla _forward_decode for short prompt

## Overview
This PR is a cherry-pick of #8263 to the v0.18.0 release branch, addressing short prompt handling issues in MLA (Multi-Head Latent Attention) by adding PrefillNoCache state in the _forward_decode method. The fix ensures proper state management for short prompts during the decode phase to handle mixed long and short prompt batches correctly.

## Technical Significance
This cherry-pick ensures consistency between main branch and release branch for short prompt handling fixes. Short prompts require special state management to avoid incorrect execution path selection, especially when mixed with longer prompts. The fix improves robustness for variable-length prompt processing across different vLLM versions.

## Related
- `technique-mla-attention`
- `technique-state-management`
- `technique-short-prompt-handling`