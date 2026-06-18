---
id: technique-pr-sgl-kernel-npu-232
title: "PR Insight: sgl-project/sgl-kernel-npu #232"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gated-delta
  - triton
  - chunk
  - attention
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/232"
---

# PR Insight: sgl-project/sgl-kernel-npu #232

**Title:** [Feat] add chunk_gated_delta_rule triton support

## Overview
Adds comprehensive Triton support for chunk_gated_delta_rule operations, including chunk_gated_delta_rule_fwd_h, chunk_fwd_o, chunk_scaled_dot_kkt_fwd, chunk_local_cumsum_scalar, solve_tril, and recompute_w_u_fwd operations.

## Technical Significance
The chunk_gated_delta_rule operations are critical for efficient attention computation in modern LLM architectures. The Triton implementations provide optimized performance for these complex operations, with current support for VARLEN with head dim 128 and chunk_size 64 (Qwen-Next-80B). This significantly improves attention computation efficiency for supported configurations.

## Related
- `wiki-kernel-attention`
- `wiki-technique-chunk-based-computation`
- `wiki-language-triton`
- `wiki-technique-gated-attention`