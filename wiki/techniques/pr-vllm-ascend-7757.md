---
id: technique-pr-vllm-ascend-7757
title: "PR Insight: vllm-project/vllm-ascend #7757"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
  - bincount
  - kernel-optimization
  - penalties
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7757"
---

# PR Insight: vllm-project/vllm-ascend #7757

**Title:** [Performance][model_runner_v2]:optimize the performance of the bincount_kernel

## Overview
This PR optimizes the bincount_kernel performance in model runner v2 for penalty computation. The optimization affects sampling penalties and token frequency counting operations.

## Technical Significance
Improves sampling performance by optimizing bincount kernel operations used for penalty calculation, reducing latency in token generation with frequency-based penalties.

## Related
- `technique-kernel-optimization`, `pattern-sampling-optimization`, `technique-penalty-computation`, `kernel-elementwise`