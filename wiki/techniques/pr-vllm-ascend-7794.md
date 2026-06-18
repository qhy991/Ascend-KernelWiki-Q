---
id: technique-pr-vllm-ascend-7794
title: "PR Insight: vllm-project/vllm-ascend #7794"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - sampling
  - penalties
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7794"
---

# PR Insight: vllm-project/vllm-ascend #7794

**Title:** [releases/v0.18.0][Triton][Sampler] Add penalty-related Triton kernel for better performance of penalties

## Overview
This PR adds penalty-related Triton kernels for improved sampling performance with penalties. The implementation includes bincount and penalty computation kernels, updating sampler logic to use optimized Triton operations.

## Technical Significance
Improves sampling performance with penalties by implementing optimized Triton kernels for frequency and presence penalty calculations, reducing latency in constrained generation scenarios.

## Related
- `technique-triton-optimization`, `pattern-sampling-optimization`, `technique-penalty-computation`, `kernel-elementwise`, `pattern-frequency-penalty`