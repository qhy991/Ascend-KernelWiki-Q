---
id: technique-pr-vllm-ascend-1990
title: "PR Insight: vllm-project/vllm-ascend #1990"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - w8a8
  - deepseek
  - vocab-parallel
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1990"
---

# PR Insight: vllm-project/vllm-ascend #1990

**Title:** [0.9.1][bugfixed] fix the bug when run the inference of quantized ds-w8a8-mtp

## Overview
This PR adds a wrapper for vocab_parallel_embedding to fix bugs when running DeepSeek-W8A8-MTP quantized inference. This is a backport of the main branch fix in PR #2134.

## Technical Significance
Critical bugfix for quantized MTP inference. The vocab_parallel_embedding wrapper ensures correct weight handling and computation for the combination of W8A8 quantization, MTP (Multi-Token Prediction), and vocabulary parallelism.

## Related
- `technique-mtp`
- `technique-w8a8-quantization`
- `technique-deepseek`
- `technique-vocab-parallel`