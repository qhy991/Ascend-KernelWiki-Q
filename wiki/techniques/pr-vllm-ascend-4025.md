---
id: technique-pr-vllm-ascend-4025
title: "PR Insight: vllm-project/vllm-ascend #4025"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mtp
  - qwen3-next
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4025"
---

# PR Insight: vllm-project/vllm-ascend #4025

**Title:** [BugFix][main] Adapted to torch_npu.npu_fused_infer_attention_score

## Overview
This PR fixes a compatibility bug with `torch_npu.npu_fused_infer_attention_score` operator that affected Qwen3-Next models with MTP enabled. The fix adapts the attention implementation to work correctly with the fused attention operator, addressing issues reported in the vllm-ascend tracker.

## Technical Significance
The `npu_fused_infer_attention_score` operator provides better performance for attention computation on Ascend NPUs. Ensuring compatibility with this operator is critical for models like Qwen3-Next that use MTP, as attention is a core operation in both main model and MTP paths. The fix enables proper use of hardware-optimized attention operations.

## Related
- `technique-attention`, `technique-mtp`, `pattern-operator-compatibility`, `technique-qwen3-next`