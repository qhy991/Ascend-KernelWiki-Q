---
id: technique-pr-vllm-ascend-7222
title: "PR Insight: vllm-project/vllm-ascend #7222"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v3.1
  - quantization
  - w8a8c8
  - kv-cache
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7222"
---

# PR Insight: vllm-project/vllm-ascend #7222

**Title:** [Feature]Supports DSv3.1 PD separation and C8 quantization

## Overview
This PR adds support for DeepSeek V3.1 W8A8C8 quantization in PD (prefill-decode) separation scenarios using MooncakeLayerwiseConnector. C8 quantizes KV cache to int8 to reduce memory usage and improve throughput. The implementation supports dynamic activation quantization and static KV cache quantization but not C8 with MTP.

## Technical Significance
This feature enables significant memory savings for DeepSeek V3.1 inference on Ascend by quantizing KV cache from BF16 to INT8, reducing KV cache memory by ~50%. It's only compatible with PD separation mode and requires ModelSlim for quantization. The integration handles weight loading, MLA attention paths, and context parallelism for the quantized model format.

## Related
- technique-kv-cache-paging
- technique-quantization
- technique-w8a8c8