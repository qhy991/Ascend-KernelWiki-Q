---
id: technique-pr-vllm-ascend-7569
title: "PR Insight: vllm-project/vllm-ascend #7569"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - sampling
  - penalties
  - kernel-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7569"
---

# PR Insight: vllm-project/vllm-ascend #7569

**Title:** [Triton][Sampler] Add penalty-related Triton kernel for better performance of penalties

## Overview
This PR implements get_token_bin_counts_and_mask and apply_penalties with Triton-Ascend kernels, significantly reducing sampling latency when repetition/frequency/presence penalties are enabled. Benchmarks show 2.5-17x speedup over previous implementations.

## Technical Significance
This optimization matters for sampling performance with penalties on Ascend. Penalty computation is expensive in Python. The Triton kernels accelerate this path, especially important for models that commonly use penalties to control repetition. Speedups range from 1.23ms to 3.29ms for various sequence/batch configurations, improving overall decode throughput.

## Related
- technique-triton
- technique-sampling