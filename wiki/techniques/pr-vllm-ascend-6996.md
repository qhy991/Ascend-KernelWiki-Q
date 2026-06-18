---
id: technique-pr-vllm-ascend-6996
title: "PR Insight: vllm-project/vllm-ascend #6996"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - context-parallel
  - fia
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6996"
---

# PR Insight: vllm-project/vllm-ascend #6996

**Title:** [Refactor] Replace npu_ring_mla with FIA in mla_cp prefill

## Overview
Refactors MLA (Multi-Layer Attention) prefill for context parallel (CP) implementation by replacing `npu_ring_mla` with `npu_fused_infer_attention_score (FIA)` operator, unifying the attention backend with standard attention implementation. Uses TND layout with `softmax_lse_flag=True` for prefill attention and extracts common functions to `common_cp.py`.

## Technical Significance
Unifies attention implementation by using FIA operator consistently across both MLA CP and standard attention, simplifying the codebase. The refactoring improves maintainability and ensures consistent behavior across different attention variants.

## Related
- `technique-mla`, `technique-fia`, `technique-context-parallel`, `technique-attention-unification`