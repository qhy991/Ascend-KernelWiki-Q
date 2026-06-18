---
id: technique-pr-vllm-ascend-2964
title: "PR Insight: vllm-project/vllm-ascend #2964"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - hybrid-kv-cache
  - shared-expert
  - torchair
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2964"
---

# PR Insight: vllm-project/vllm-ascend #2964

**Title:** [bugfix] fix shared expert dp with hybrid kvcache

## Overview
This PR fixes a RuntimeError when using shared_expert_dp with enforce_eager mode and hybrid KV cache. The issue occurred because set_forward_context with shared_expert_dp fell back to model_runner_v1.py implementation, setting attn_metadata as a dictionary, which caused type errors in torchair_deepseek_v2.py.

## Technical Significance
The fix introduces attention metadata transformation to ensure compatibility between different execution paths. It addresses the interaction between shared expert data parallelism, hybrid KV cache, and eager mode, which are critical for DeepSeek models with shared experts.

## Related
- `kernel-moe-ascendc`, `technique-hybrid-kv-cache`, `technique-shared-expert-dp`