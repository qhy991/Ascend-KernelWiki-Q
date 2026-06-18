---
id: technique-pr-vllm-ascend-4830
title: "PR Insight: vllm-project/vllm-ascend #4830"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - rejection-sampling
  - greedy-sample
  - expand-kernel
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4830"
---

# PR Insight: vllm-project/vllm-ascend #4830

**Title:** feat: implement high-performance Triton kernels for rejection sampling

## Overview
This PR introduces optimized Triton implementations for rejection_greedy_sample_kernel and expand_kernel. The new kernels (rejection_greedy_sample_spec_len_1_triton and rejection_greedy_sample_triton) deliver superior performance across various batch sizes and MTP configurations while maintaining full functional accuracy.

## Technical Significance
Improves rejection sampling performance critical for speculative decoding (MTP). The optimized Triton kernels reduce latency in the token acceptance verification and candidate expansion phases, accelerating speculative decoding throughput.

## Related
- `kernel-rejection-sampler`
- `kernel-rejection-greedy-sample`
- `kernel-expand`
- `technique-speculative-decoding`
- `kernel-mtp`