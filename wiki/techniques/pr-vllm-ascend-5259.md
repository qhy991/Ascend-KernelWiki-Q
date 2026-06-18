---
id: technique-pr-vllm-ascend-5259
title: "PR Insight: vllm-project/vllm-ascend #5259"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - triton
  - rejection-sampling
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5259"
---

# PR Insight: vllm-project/vllm-ascend #5259

**Title:** feat: implement high-performance Triton kernels for rejection sampling: optimization for rejection_random_sample_kernel

## Overview
This PR introduces optimized Triton implementations for rejection sampling kernels, specifically optimizing `rejection_random_sample_kernel`. The new implementations deliver significant performance improvements across various batch sizes and MTP configurations while maintaining functional accuracy.

## Technical Significance
Rejection sampling is critical for MTP performance and speculative decoding. The optimized Triton kernels show up to 4-6x speedup for large batch sizes (2048), dramatically improving MTP inference throughput on Ascend NPUs. This optimization enables better utilization of Ascend hardware for sampling-intensive workloads.

## Related
- technique-triton-optimization
- technique-mtp
- technique-speculative-decoding