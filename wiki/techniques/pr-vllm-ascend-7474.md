---
id: technique-pr-vllm-ascend-7474
title: "PR Insight: vllm-project/vllm-ascend #7474"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gqa
  - kv-cache
  - c8-quantization
  - int8
  - fia
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7474"
---

# PR Insight: vllm-project/vllm-ascend #7474

**Title:** feat(quant): add C8 INT8 KV cache support for GQA attention models

## Overview
This PR adds C8 (INT8) KV cache quantization support for standard GQA attention models like Qwen3-32B W8A8C8. It introduces AscendC8AttentionBackendImpl, AscendC8KVCacheAttentionMethod, and integration with modelslim_config. C8 uses static per-channel quantization to store KV cache in INT8, reducing memory by ~50% compared to BF16.

## Technical Significance
This feature matters for memory efficiency on Ascend. By quantizing KV cache from BF16 to INT8, it enables higher batch concurrency and longer context lengths. The implementation includes per-channel scale/offset handling, FIA V1 BNSD paged attention with native INT8 KV, and separate decode/prefill kernel calls. Benchmarks show 1445.85 tok/s throughput at max_concurrency=192 with 131k context length.

## Related
- technique-quantization
- technique-kv-cache-paging
- technique-w8a8c8
- technique-gqa