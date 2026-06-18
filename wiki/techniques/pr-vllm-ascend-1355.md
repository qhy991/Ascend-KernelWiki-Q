---
id: technique-pr-vllm-ascend-1355
title: "PR Insight: vllm-project/vllm-ascend #1355"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - gating
  - fused-ops
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1355"
---

# PR Insight: vllm-project/vllm-ascend #1355

**Title:** use npu_moe_gating_top_k_softmax

## Overview
This PR replaces manual MoE gating top-k and softmax computation with the fused `npu_moe_gating_top_k_softmax` operator.

## Technical Significance
Improves MoE gating performance by using Ascend's fused operator that combines top-k selection and softmax activation in a single kernel. This reduces kernel launch overhead and improves memory locality, which is critical for the gating computation that determines expert selection for each token.

## Related
- `kernel-moe`
- `technique-operator-fusion`
- `technique-gating`