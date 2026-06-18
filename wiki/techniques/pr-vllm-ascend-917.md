---
id: technique-pr-vllm-ascend-917
title: "PR Insight: vllm-project/vllm-ascend #917"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - padding
  - performance
  - v1-engine
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/917"
---

# PR Insight: vllm-project/vllm-ascend #917

**Title:** [Perf]remove unnecessary padding before MLA V1 prefill

## Overview
This PR removes unnecessary padding of q, k, v tensors to head_dim 256 in MLA V1 prefill. The new MLA kernel supports non-128-divisible head_dims, eliminating the need for padding and improving performance.

## Technical Significance
Unnecessary padding increases memory usage and computation. By removing padding that was only required for early MLA kernels, this PR reduces memory footprint and computation overhead for MLA V1 prefill operations, directly improving inference performance.

## Related
- `kernel-mla`
- `technique-padding`
- `kernel-prefill`