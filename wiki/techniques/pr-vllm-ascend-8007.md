---
id: technique-pr-vllm-ascend-8007
title: "PR Insight: vllm-project/vllm-ascend #8007"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - kv-cache
  - c8
  - int8
  - gqa
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8007"
---

# PR Insight: vllm-project/vllm-ascend #8007

**Title:** [v0.18.0]feat(quant): add C8 INT8 KV cache support for GQA attention models

## Overview
This PR adds C8 (INT8) KV cache quantization support for standard GQA attention models like Qwen3-32B W8A8C8. The implementation includes `AscendC8AttentionBackendImpl` with per-channel quantization, `_prepare_c8_scales` for scale sharding, `_quantize_kv_to_int8` for BF16 to INT8 conversion, and separate decode and prefill kernels. The feature reduces KV cache memory by ~50% compared to BF16.

## Technical Significance
KV cache quantization is critical for serving larger models and higher batch sizes. The C8 scheme uses static per-channel scales with INT8 storage, enabling significant memory savings. The implementation covers all attention states including PrefillNoCache, PrefillCacheHit, ChunkedPrefill, and DecodeOnly. Benchmarking shows successful serving of Qwen3-32B W8A8C8 with 1445.85 tok/s throughput and 192 max concurrency.

## Related
- `kernel-attention`
- `technique-quantization`
- `technique-kv-cache-paging`
- `quantization-c8`