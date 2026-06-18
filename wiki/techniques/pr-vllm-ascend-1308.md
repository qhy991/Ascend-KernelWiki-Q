---
id: technique-pr-vllm-ascend-1308
title: "PR Insight: vllm-project/vllm-ascend #1308"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - fused-ops
  - sampling
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1308"
---

# PR Insight: vllm-project/vllm-ascend #1308

**Title:** [Perf] Use fused ops npu_top_k_top_p

## Overview
This PR replaces manual top-k and top-p sampling computation with the fused `npu_top_k_top_p` operator, reducing kernel launch overhead and improving sampling performance.

## Technical Significance
Improves sampling throughput by using Ascend's fused top-k and top-p operator instead of separate kernel launches. The fused operator performs both operations in a single kernel invocation, reducing memory access and synchronization overhead. This is particularly beneficial for high-throughput inference scenarios where sampling is a bottleneck.

## Related
- `technique-operator-fusion`
- `technique-sampling`