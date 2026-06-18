---
id: technique-pr-vllm-ascend-9703
title: "PR Insight: vllm-project/vllm-ascend #9703"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - mla
  - eagle3
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9703"
---

# PR Insight: vllm-project/vllm-ascend #9703

**Title:** [BugFix][SpecDecode] Fix MLA shape mismatch with Eagle3 and add DeepSeek V2 Eagle3 support

## Overview
This PR fixes MLA `hidden_dim` shape mismatch with Eagle3 speculative decoding and adds `Eagle3DeepseekV2ForCausalLM` support. The shape mismatch occurred because `hidden_dim` was derived from `hidden_states.shape[-1]` which doesn't always equal `self.hidden_size` when Eagle3 calls `combine_hidden_states`.

## Technical Significance
Fixes shape compatibility issues between MLA and Eagle3 speculative decoding by using `self.hidden_size` directly and constructing output shape explicitly. Enables DeepSeek V2 models to work with Eagle3 spec decode by adding the missing model type check. Validated with Kimi-K2.5-Thinking-Eagle3 on 2×A3 with DP=32, TP=1, EP=32, W4A8 quantization.

## Related
- `technique-spec-decode`, `kernel-mla`, `technique-eagle3`