---
id: technique-pr-vllm-ascend-9830
title: "PR Insight: vllm-project/vllm-ascend #9830"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qkv-split
  - rmsnorm
  - rope
  - triton
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9830"
---

# PR Insight: vllm-project/vllm-ascend #9830

**Title:** [Performance] Optimize split_qkv_tp_rmsnorm_rope with grid stride andh loading

## Overview
This PR optimizes the split_qkv_tp_rmsnorm_rope operation using grid stride and H (hidden dimension) loading techniques. It improves memory access patterns and computational efficiency for the combined QKV split, RMS normalization, and RoPE operation.

## Technical Significance
Improves performance of QKV projection, normalization, and rotation fusion through optimized memory access patterns using grid stride and efficient H-dimension loading. Reduces memory bandwidth pressure and improves cache utilization on Ascend NPUs.

## Related
- `kernel-qkv-split`, `kernel-rmsnorm`, `kernel-rope`, `technique-operator-fusion`