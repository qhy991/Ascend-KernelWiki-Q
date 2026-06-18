---
id: technique-pr-vllm-ascend-4158
title: "PR Insight: vllm-project/vllm-ascend #4158"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunk-prefill
  - long-sequence
  - mla
  - attention
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4158"
---

# PR Insight: vllm-project/vllm-ascend #4158

**Title:** [long_seq_Feat] support chunk prefill

## Overview
This PR adds chunk prefill support for long sequences, including: (1) Qwen GQA attention_v1 optimization, (2) DeepSeek MLA refactoring to use all_gather kv instead of all_gather q, (3) Model runner refactoring for chunk prefill to remove unused code. The changes enable efficient processing of long sequences by chunking the prefill phase.

## Technical Significance
Chunk prefill is essential for handling long sequences efficiently, reducing memory pressure and improving throughput. Refactoring MLA to all_gather KV instead of Q reduces communication overhead in distributed scenarios. The model runner cleanup simplifies the codebase and removes unnecessary complexity for chunk prefill scenarios.

## Related
- `technique-chunk-prefill`, `technique-long-sequence`, `technique-mla`, `technique-attention`, `pattern-refactoring`