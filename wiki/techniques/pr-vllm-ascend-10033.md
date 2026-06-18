---
id: technique-pr-vllm-ascend-10033
title: "PR Insight: vllm-project/vllm-ascend #10033"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - scaled-dot-product
  - triton
  - accuracy
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10033"
---

# PR Insight: vllm-project/vllm-ascend #10033

**Title:** [BugFix] chunk_scaled_dot_kkt_fwd_kernel accuracy issues

## Overview
This PR fixes accuracy issues in the chunk_scaled_dot_kkt_fwd_kernel Triton kernel, which computes scaled dot product attention with chunked processing. The kernel had numerical precision problems affecting model accuracy.

## Technical Significance
Resolves numerical accuracy issues in the chunked scaled dot product kernel, ensuring that attention computations maintain numerical precision. Critical for maintaining model accuracy, especially for models sensitive to attention computation precision.

## Related
- `kernel-attention`, `kernel-triton`, `kernel-scaled-dot-product`, `pattern-accuracy`