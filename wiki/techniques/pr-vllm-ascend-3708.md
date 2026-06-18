---
id: technique-pr-vllm-ascend-3708
title: "PR Insight: vllm-project/vllm-ascend #3708"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mrope
  - rotary-embedding
  - qwen2.5-vl
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3708"
---

# PR Insight: vllm-project/vllm-ascend #3708

**Title:** [Feat] Add mrope fusion op

## Overview
This PR adds MRoPE (Multi-head Rotary Position Embedding) fusion operator for Qwen2.5-VL models. The fusion operator is implemented in `vllm_ascend/ops/rotary_embedding.py` with 35 lines added and 1 line removed, along with 85 lines of test coverage. Note that this operator doesn't currently support Qwen3-VL.

## Technical Significance
MRoPE fusion improves performance by combining multiple position embedding operations into a single kernel, reducing memory bandwidth and kernel launch overhead. This is particularly valuable for vision-language models like Qwen2.5-VL that process multi-modal inputs with complex position requirements. The re-introduction of MRoPE (after previous revert #3562) suggests accuracy issues have been resolved.

## Related
- `technique-mrope`
- `technique-rotary-embedding`
- `technique-operator-fusion`