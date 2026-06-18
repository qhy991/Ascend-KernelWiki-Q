---
id: technique-pr-vllm-ascend-7819
title: "PR Insight: vllm-project/vllm-ascend #7819"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - batch-transfer
  - performance
  - c++
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7819"
---

# PR Insight: vllm-project/vllm-ascend #7819

**Title:** [Performance]Batch kvcache offloading via aclrtMemcpyBatchAsync

## Overview
This PR implements batch KV cache offloading using `aclrtMemcpyBatchAsync` for CANN 8.5.0+, while maintaining backward compatibility with `aclrtMemcpyAsync` for older CANN versions. The feature allows automatic or manual selection of the appropriate transfer function based on the CANN environment, with environment variable `VLLM_ASCEND_ENABLE_BATCH_MEMCPY` for manual override.

## Technical Significance
KV cache offloading to CPU is critical for serving larger models and higher batch sizes. The batch memory copy API reduces transfer overhead by batching multiple memcpy operations, resulting in significant performance improvements. Benchmarks show TTFT improvement from 307ms to 272.82ms and TPOT improvement from 49.96ms to 41.04ms on Qwen3-14B, demonstrating the value of batching host-device transfers.

## Related
- `technique-kv-offload`
- `technique-batch-transfer`
- `pattern-kv-cache-paging`