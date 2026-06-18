---
id: technique-pr-sgl-kernel-npu-389
title: "PR Insight: sgl-project/sgl-kernel-npu #389"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - batched-execution
  - mamba
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/389"
---

# PR Insight: sgl-project/sgl-kernel-npu #389

**Title:** Supports batched causal_conv1d

## Overview
This PR adds support for batched execution of causal_conv1d operations, eliminating the need for explicit loops in Python. The implementation is tested with Qwen3-Next-80B-A3B-Instruct, showing 1.02-1.86x speedup across different scenarios and maintaining accuracy (gsm8k: 0.937-0.941 before/after).

## Technical Significance
Batching causal_conv1d operations significantly reduces kernel launch overhead and improves end-to-end latency, especially for short sequences where TTFT improvements of up to 3.16x are observed. This optimization is particularly valuable for Mamba-style attention in models like Qwen3-Next, improving both prefill and decode performance.

## Related
- `kernel-causal-conv1d`, `kernel-mamba`, `technique-batching`, `technique-latency-optimization`