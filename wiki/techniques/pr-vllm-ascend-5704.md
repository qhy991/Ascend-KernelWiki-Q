---
id: technique-pr-vllm-ascend-5704
title: "PR Insight: vllm-project/vllm-ascend #5704"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - attention
  - fused-infer-attention
  - bfloat16
  - context-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5704"
---

# PR Insight: vllm-project/vllm-ascend #5704

**Title:** [Refactor] Replace npu_ring_mla with FIA in MLA prefill

## Overview
This PR refactors the Multi-Layer Attention (MLA) prefill implementation by replacing the `npu_ring_mla` operator with `npu_fused_infer_attention_score` (FIA) operator, unifying the attention backend with standard attention implementation. The changes affect `mla_v1.py` where the prefill forward and context computation now use FIA with TND layout, automatic float16 to bfloat16 conversion, and `npu_attention_update` for LSE-based output merging. Context Parallel compatibility is maintained through a dedicated `_ring_mla_mask_builder`.

## Technical Significance
This refactoring aligns MLA prefill with standard attention (`attention_v1.py`) for better code maintainability and future compatibility. The key optimization moves metadata pre-computation (cumsum operations) from forward pass to metadata building phase, and uses FIA's native LSE support for chunked context merging. The automatic dtype conversion addresses FIA's TND layout constraint requiring bfloat16, ensuring consistent behavior while unifying the attention implementation across the codebase.

## Related
- `technique-operator-fusion`, `technique-pipeline-scheduling`, `hw-cube-unit`, `hw-vector-unit`, `technique-context-parallel`