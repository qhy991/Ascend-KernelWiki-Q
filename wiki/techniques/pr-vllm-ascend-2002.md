---
id: technique-pr-vllm-ascend-2002
title: "PR Insight: vllm-project/vllm-ascend #2002"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - vectorization
  - sampling
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2002"
---

# PR Insight: vllm-project/vllm-ascend #2002

**Title:** [v0.9.1][RejectSampler][Perf] Optimize greedy reject sampler with vectorization.

## Overview
This PR optimizes the greedy reject sampler by rewriting `rejection_greedy_sample_pytorch` function from a loop-based implementation to a vectorized form. A specialized function `rejection_greedy_sample_spec_len_1_pytorch` is provided for all-greedy scenarios with `spec_len==1` for maximum efficiency.

## Technical Significance
Vectorization provides significant performance improvements, especially in large batch size scenarios where loop-based sampling becomes a bottleneck. By leveraging PyTorch's vectorized operations, this PR reduces sampling overhead and improves overall inference throughput for speculative decoding workloads.

## Related
- `technique-spec-decode`
- `technique-vectorization`
- `technique-sampling`