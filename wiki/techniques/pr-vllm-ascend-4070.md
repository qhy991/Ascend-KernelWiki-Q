---
id: technique-pr-vllm-ascend-4070
title: "PR Insight: vllm-project/vllm-ascend #4070"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - triton
  - chunk-gated-delta-rule
  - performance
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4070"
---

# PR Insight: vllm-project/vllm-ascend #4070

**Title:** 【OPS】qwen3-next support triton chunk_gated_delta_rule ops

## Overview
This PR adds Triton chunk_gated_delta_rule operators support for Qwen3-Next, including chunk, chunk_delta_h, chunk_o, chunk_scaled_dot_kkt, cumsum, solve_tril, wy_fast, and utils operators. The implementation provides more than 2x reduction in TTFT (Time To First Token) by optimizing the chunked computation patterns specific to Qwen3-Next architecture.

## Technical Significance
Triton kernels provide flexible, high-performance computation for complex patterns like chunk_gated_delta_rule. The TTFT reduction of over 2x demonstrates significant performance improvement for prefill phase operations. Custom Triton operators enable better hardware utilization than generic PyTorch operations for model-specific patterns.

## Related
- `technique-triton`, `pattern-custom-ops`, `technique-qwen3-next`, `technique-prefill-optimization`