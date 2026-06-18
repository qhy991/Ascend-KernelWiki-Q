---
id: technique-pr-sgl-kernel-npu-130
title: "PR Insight: sgl-project/sgl-kernel-npu #130"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mamba
  - elementwise
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/130"
---

# PR Insight: sgl-project/sgl-kernel-npu #130

**Title:** update qwen3-next performance kernels

## Overview
This PR updates performance kernels for Qwen3-Next model, including fused sigmoid gating recurrent kernels and causal conv1d operations used in Mamba-style architectures.

## Technical Significance
Qwen3-Next optimized kernels ensure efficient inference for state-of-the-art language models. Fused sigmoid gating and causal conv1d are critical for Mamba architectures, and their optimization directly impacts throughput and latency for sequential modeling tasks.

## Related
- `kernel-attention-ascendc`, `technique-operator-fusion`