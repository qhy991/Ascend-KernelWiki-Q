---
id: technique-pr-vllm-ascend-461
title: "PR Insight: vllm-project/vllm-ascend #461"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - performance
  - mask
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/461"
---

# PR Insight: vllm-project/vllm-ascend #461

**Title:** [ModelRunner][V1] Optimize V1 attention mask

## Overview
This PR is a cherry-pick of #442, optimizing V1 attention mask construction by pre-constructing mask matrices. The implementation adds environment variable configuration for tuning mask matrix size.

## Technical Significance
Attention mask construction is per-request overhead. Pre-constructing masks trades memory for computation, improving throughput for long-context scenarios. The environment variable allows balancing memory usage and performance based on NPU capacity.

## Related
- kernel-attention
- technique-performance-optimization