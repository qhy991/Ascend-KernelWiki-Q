---
id: technique-pr-vllm-ascend-9849
title: "PR Insight: vllm-project/vllm-ascend #9849"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - qkv-split
  - rmsnorm
  - rope
  - triton
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9849"
---

# PR Insight: vllm-project/vllm-ascend #9849

**Title:** [Ascend950] [BugFix] Fix split_qkv_rmsnorm_rope Triton kernel accuracy issue on A5

## Overview
This PR fixes accuracy issues in the split_qkv_rmsnorm_rope Triton kernel on Ascend A5 devices. The kernel combines QKV split, RMS normalization, and RoPE operations, but had precision problems affecting model accuracy.

## Technical Significance
Resolves numerical accuracy issues in the fused QKV split, normalization, and rotation kernel on A5 devices. Ensures that model outputs remain numerically correct when using this optimized Triton kernel, maintaining inference quality.

## Related
- `kernel-qkv-split`, `kernel-rmsnorm`, `kernel-rope`, `kernel-triton`, `technique-operator-fusion`