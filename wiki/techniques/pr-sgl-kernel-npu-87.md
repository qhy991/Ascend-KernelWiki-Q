---
id: technique-pr-sgl-kernel-npu-87
title: "PR Insight: sgl-project/sgl-kernel-npu #87"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fla
  - mamba
  - attention
  - causal-conv1d
  - python-kernels
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/87"
---

# PR Insight: sgl-project/sgl-kernel-npu #87

**Title:** [Feature] add fla and mamba kernels

## Overview
This PR adds Flash Linear Attention (FLA) and Mamba kernel implementations for Ascend NPU. Includes chunk attention (162 lines), fused sigmoid gating recurrent (236 lines), and causal conv1d (550 lines) kernels. These enable efficient inference of state-space models and linear attention variants.

## Technical Significance
Expands inference kernel coverage beyond standard transformer attention to support advanced architectures like Mamba (selective state-space models) and Flash Linear Attention. These kernels enable efficient execution of emerging LLM architectures on Ascend hardware, critical for supporting next-generation model families.

## Related
- technique-flash-attention
- technique-mamba
- technique-state-space-models
- technique-linear-attention