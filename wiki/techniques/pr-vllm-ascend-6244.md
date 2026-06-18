---
id: technique-pr-vllm-ascend-6244
title: "PR Insight: vllm-project/vllm-ascend #6244"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - w8a8
  - quantization
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6244"
---

# PR Insight: vllm-project/vllm-ascend #6244

**Title:** [TEST]add a qwen3-30b acc case with mooncake mempool

## Overview
This PR adds a weekly accuracy test case for Qwen3-30B with W8A8 quantization using Mooncake memory pool. The test is added to the scheduled nightly test workflow and covers the W8A8 quantized model in Mooncake distributed inference scenarios.

## Technical Significance
Regular accuracy testing for quantized models (W8A8) with Mooncake ensures that weight8/activation8 quantization doesn't degrade output quality in distributed inference setups. Memory pool testing validates that Mooncake's KV cache management works correctly with quantized models, which is critical for production deployment of large quantized models.

## Related
- `technique-mooncake`, `technique-quantization`, `technique-w8a8`, `technique-testing`