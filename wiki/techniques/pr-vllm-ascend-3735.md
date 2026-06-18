---
id: technique-pr-vllm-ascend-3735
title: "PR Insight: vllm-project/vllm-ascend #3735"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mrope
  - rotary-embedding
  - qwen2.5-vl
  - operator-fusion
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3735"
---

# PR Insight: vllm-project/vllm-ascend #3735

**Title:** [cherry-pick][Feat] Add mrope fusion op#3708

## Overview
This is a cherry-pick of PR #3708 to the release branch, adding MRoPE (Multi-head Rotary Position Embedding) fusion operator for Qwen2.5-VL models. The implementation adds 35 lines to `vllm_ascend/ops/rotary_embedding.py` and 85 lines of test coverage. The operator doesn't currently support Qwen3-VL.

## Technical Significance
Cherry-picking MRoPE fusion to release branches ensures users get performance improvements for Qwen2.5-VL workloads. MRoPE fusion reduces kernel launch overhead and memory bandwidth by combining multiple position embedding operations, valuable for vision-language models with complex position requirements.

## Related
- `technique-mrope`
- `technique-rotary-embedding`
- `technique-operator-fusion`