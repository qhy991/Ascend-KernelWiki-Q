---
id: technique-pr-vllm-ascend-7767
title: "PR Insight: vllm-project/vllm-ascend #7767"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
  - sampling
  - ranks-kernel
  - min-p-kernel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7767"
---

# PR Insight: vllm-project/vllm-ascend #7767

**Title:** [Performance][model_runner_v2]:optimize the performance of the _ranks_kernel and _min_p_kernel

## Overview
This PR optimizes the performance of _ranks_kernel and _min_p_kernel in model runner v2 for sampling operations. The changes affect top-k logprobs computation and min-p sampling implementation.

## Technical Significance
Improves sampling performance by optimizing rank computation and min-p filtering kernels, reducing latency in advanced sampling strategies like top-k and min-p nucleus sampling.

## Related
- `technique-sampling-optimization`, `pattern-top-k-sampling`, `pattern-min-p-sampling`, `kernel-elementwise`, `technique-kernel-optimization`