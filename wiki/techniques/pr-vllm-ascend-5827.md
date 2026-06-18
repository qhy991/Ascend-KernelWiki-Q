---
id: technique-pr-vllm-ascend-5827
title: "PR Insight: vllm-project/vllm-ascend #5827"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - rotary-embedding
  - multimodal
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5827"
---

# PR Insight: vllm-project/vllm-ascend #5827

**Title:** [Performance]use triton mrope for Qwen3-VL

## Overview
This PR optimizes rotary position embedding (RoPE) performance for Qwen3-VL multimodal models by using a Triton kernel instead of the native implementation. Benchmarking shows significant improvements: for Qwen3-VL-235B-A22B-Instruct-W8A8, TTFT drops from 4.8771s to 4.3273s, TPOT from 0.1472s to 0.0615s, and throughput increases from 49 to 105 tokens/s.

## Technical Significance
The Triton mrope kernel provides substantial performance gains for multimodal vision-language models. The optimization is particularly impactful for large models with high-resolution image inputs. Testing on Qwen3-VL-8B-Instruct shows similar gains: TTFT improves from 4.1744s to 3.1858s, TPOT from 0.0499s to 0.0245s, and throughput doubles from 125 to 227 tokens/s. The implementation requires Triton-ascend 3.2.0.dev20260105 and is enabled through the rotary_embedding.py module.

## Related
- `technique-triton`, `technique-rotary-embedding`, `technique-multimodal-optimization`