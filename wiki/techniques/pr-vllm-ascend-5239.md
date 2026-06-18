---
id: technique-pr-vllm-ascend-5239
title: "PR Insight: vllm-project/vllm-ascend #5239"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - fia
  - sliding-window
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5239"
---

# PR Insight: vllm-project/vllm-ascend #5239

**Title:** [feature] fia support sliding windows

## Overview
This PR enables FIA (Fused Infer Attention) to support sliding window attention functionality by modifying the `forward_fused_infer_attention` function. The implementation adapts FIA for models like Gemma3 that require sliding window constraints.

## Technical Significance
Sliding window attention reduces memory and compute requirements by limiting attention to a local context window. Enabling this for FIA brings performance benefits of fused attention kernels to sliding window models on Ascend NPUs, improving efficiency for long-context workloads with sliding window patterns.

## Related
- technique-fia
- technique-sliding-window
- technique-flash-attention