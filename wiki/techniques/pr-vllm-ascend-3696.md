---
id: technique-pr-vllm-ascend-3696
title: "PR Insight: vllm-project/vllm-ascend #3696"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fia
  - prefill
  - cache-mode
  - full-graph
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3696"
---

# PR Insight: vllm-project/vllm-ascend #3696

**Title:** support prefill cache mode use fia op

## Overview
This PR enables FIA (Flash-Inference-Attention) operator usage in prefill cache mode for full graph execution. Changes were made to `vllm_ascend/attention/attention_v1.py` (37 additions, 12 deletions), `vllm_ascend/worker/model_runner_v1.py`, and `vllm_ascend/attention/attention_mask.py`. Benchmark results show throughput improvement from 466.77 to 472.26 tok/s.

## Technical Significance
FIA operators provide optimized attention computation, but weren't previously used in prefill cache mode. Enabling FIA for this mode improves prefill performance by leveraging hardware-optimized kernels. The benchmark shows ~1.2% throughput improvement, demonstrating the benefit of using FIA across more execution modes in full-graph scenarios.

## Related
- `technique-fia`
- `technique-prefill`
- `technique-full-graph`