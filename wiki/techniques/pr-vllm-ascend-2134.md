---
id: technique-pr-vllm-ascend-2134
title: "PR Insight: vllm-project/vllm-ascend #2134"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - mtp
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2134"
---

# PR Insight: vllm-project/vllm-ascend #2134

**Title:** [bugfixed] fix the bug when run the inference of quantized ds-w8a8-mtp

## Overview
This PR fixes a bug where `ParallelLMhead` has no attribute `params_dtype` when running inference of quantized DeepSeek w8a8 MTP (speculative decoding). The fix adds a wrapper for `vocab_parallel_embedding` and modifies `vllm_ascend/quantization/func_wrapper.py` and `vllm_ascend/quantization/quantizer.py`.

## Technical Significance
This bugfix resolves compatibility issues between quantization (w8a8) and speculative decoding (MTP) in DeepSeek models. The wrapper pattern ensures proper dtype handling for parallel vocabulary embeddings, which is critical for quantized models where precision management is essential. The fix enables correct inference of quantized DeepSeek models with MTP enabled.

## Related
- `technique-quantization-w8a8`, `technique-speculative-decoding`, `kernel-vocab-parallel-embedding-ascendc`