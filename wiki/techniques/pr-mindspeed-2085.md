---
id: technique-pr-mindspeed-2085
title: "PR Insight: Ascend/MindSpeed #2085"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - tensor-parallel
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2085"
---

# PR Insight: Ascend/MindSpeed #2085

**Title:** refactor:moe:tp_extend_ep and gemm and shared_expert

## Overview
This PR refactors MoE (Mixture of Experts) implementations including tp_extend_ep (tensor parallel extend expert parallel), GEMM operations, and shared expert handling. The change improves the efficiency and maintainability of MoE training on Ascend NPUs.

## Technical Significance
MoE refactoring is critical for efficient training of large-scale mixture-of-experts models on Ascend hardware. The tp_extend_ep feature enables hybrid parallel strategies that combine tensor parallel with expert parallel, improving scalability for models with many experts. Optimizing GEMM operations for MoE routing and shared expert handling improves computational efficiency and reduces communication overhead. These optimizations are essential for achieving good performance on MoE models, which are increasingly important for scaling language models.

## Related
- `technique-cube-vector-overlap`
- `technique-hccl-optimization`