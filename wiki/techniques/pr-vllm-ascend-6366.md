---
id: technique-pr-vllm-ascend-6366
title: "PR Insight: vllm-project/vllm-ascend #6366"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kernel
  - ascendc
  - kv-transfer
  - gqa
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6366"
---

# PR Insight: vllm-project/vllm-ascend #6366

**Title:** [Kernel] Add AscendC fused op transpose_kv_cache_by_block to speed up GQA transfer

## Overview
This PR implements an AscendC fused operator `transpose_kv_cache_by_block` to optimize KV cache layout transposition for GQA (Grouped Query Attention) in prefill/decode disaggregated scenarios. The fused operator replaces the previous inefficient three-op sequence (npu_paged_cache_load + transpose + npu_reshape_and_cache).

## Technical Significance
The optimization reduces kernel launches from 3*layer_num to 1*layer_num and data movement between L1 cache and HBM from 6*layer_num to 1*layer_num per request. Performance tests show a 28x speedup (7ms to 0.24ms) for the transpose operation and 90-110ms TTFT improvement for Qwen3-235B in PD disaggregation scenarios.

## Related
- `technique-kv-cache`
- `technique-gqa`
- `technique-ascendc`
- `technique-operator-fusion`