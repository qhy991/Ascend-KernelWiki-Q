---
id: technique-pr-sgl-kernel-npu-214
title: "PR Insight: sgl-project/sgl-kernel-npu #214"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - zero-experts
  - identity
  - optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/214"
---

# PR Insight: sgl-project/sgl-kernel-npu #214

**Title:** add zero_experts_compute_identity

## Overview
Implements zero_experts_compute_identity functionality to handle cases where certain experts receive no tokens. This identity operation ensures correct computation when experts are unused in a given batch.

## Technical Significance
Zero expert handling is critical for MoE robustness, as not all experts receive tokens in every batch. The identity operation prevents computation errors and maintains correct output shapes when experts are idle, ensuring stable MoE operation across varying load distributions and expert selection patterns.

## Related
- `wiki-kernel-moe`
- `wiki-technique-load-balancing`
- `wiki-technique-edge-case-handling`
- `wiki-technique-identity-operations`