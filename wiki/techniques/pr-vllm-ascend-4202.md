---
id: technique-pr-vllm-ascend-4202
title: "PR Insight: vllm-project/vllm-ascend #4202"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - qwen3-next
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4202"
---

# PR Insight: vllm-project/vllm-ascend #4202

**Title:** [Cherry-pick][0.11.0] Adapted to torch_npu.npu_fused_infer_attention_score

## Overview
This PR is a cherry-pick to v0.11.0 of PR #4025, fixing the same compatibility bug with `torch_npu.npu_fused_infer_attention_score` operator that affected Qwen3-Next models. The fix adapts the attention implementation to work correctly with the fused attention operator.

## Technical Significance
Cherry-picking critical compatibility fixes ensures stability across vLLM versions. The fused attention operator provides better performance on Ascend NPUs, and the fix ensures v0.11.0 users can benefit from it without correctness issues.

## Related
- `technique-attention`, `pattern-operator-compatibility`, `technique-qwen3-next`, `technique-version-compatibility`