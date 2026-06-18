---
id: technique-pr-vllm-ascend-5818
title: "PR Insight: vllm-project/vllm-ascend #5818"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cleanup
  - attention
  - code-quality
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5818"
---

# PR Insight: vllm-project/vllm-ascend #5818

**Title:** [Cleanup] Remove dead code make_attention_mask function

## Overview
This PR removes the unused `make_attention_mask` function from `vllm_ascend/worker/v2/attn_utils.py`. Following PR #4870's attention mask unification refactor, mask generation was centralized in the `AttentionMaskBuilder` singleton class, making the old function obsolete.

## Technical Significance
Dead code removal improves maintainability and reduces code bloat. The `make_attention_mask` function was no longer called anywhere after the refactor, which consolidated mask generation into metadata builders like `AscendAttentionMetadataBuilder` and `AscendMLAMetadataBuilder`. The cleanup removes 24 lines of dead code, ensuring the codebase stays aligned with the new centralized architecture without any functional changes.

## Related
- `technique-attention-mask`, `technique-code-maintenance`