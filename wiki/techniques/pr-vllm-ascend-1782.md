---
id: technique-pr-vllm-ascend-1782
title: "PR Insight: vllm-project/vllm-ascend #1782"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - performance
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1782"
---

# PR Insight: vllm-project/vllm-ascend #1782

**Title:** [0.9.1]optmize rope in qwen2

## Overview
This PR optimizes the Rotary Position Embedding (RoPE) operation in Qwen2 models by extracting index_select operations from individual layers into the model level. This reduces (layer_num - 1) * 2 Gather operations per prefill/decode stage.

## Technical Significance
Operator fusion optimization that eliminates redundant index operations. Moving RoPE position indexing outside the loop over layers significantly reduces the number of Gather operations, which is particularly impactful for deep models with many layers.

## Related
- `kernel-rope-ascendc`
- `technique-operator-fusion`
- `technique-qwen2`