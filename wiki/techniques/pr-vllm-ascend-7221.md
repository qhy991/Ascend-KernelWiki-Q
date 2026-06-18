---
id: technique-pr-vllm-ascend-7221
title: "PR Insight: vllm-project/vllm-ascend #7221"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - topk
  - softmax
  - kernel-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7221"
---

# PR Insight: vllm-project/vllm-ascend #7221

**Title:** [model_runner_v2]optimize the performance of the _topk_log_softmax_kernel

## Overview
This PR optimizes the performance of the Triton operator _topk_log_softmax_kernel in model_runner_v2, achieving 7% of its original execution time. The optimization targets the sampling path where top-k selection is combined with log softmax computation.

## Technical Significance
This optimization matters for Ascend inference latency in the sampling stage. The topk_log_softmax kernel is performance-critical for token generation - by optimizing this Triton operator to ~1/14 of original time, it significantly reduces decode step overhead. The optimization likely involves improved memory access patterns, better vector utilization, or kernel fusion techniques to reduce memory transfers between NPU and HBM.

## Related
- technique-triton
- kernel-sampling