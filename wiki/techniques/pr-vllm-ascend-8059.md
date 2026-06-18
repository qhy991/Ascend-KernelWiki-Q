---
id: technique-pr-vllm-ascend-8059
title: "PR Insight: vllm-project/vllm-ascend #8059"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - split-qkv
  - rmsnorm
  - rope
  - operator-fusion
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8059"
---

# PR Insight: vllm-project/vllm-ascend #8059

**Title:** [Performance] optimize split_qkv_tp_rmsnorm_rope ops

## Overview
This PR optimizes the split_qkv_tp_rmsnorm_rope Triton kernels in vllm-ascend, achieving significant performance improvements for the prefill phase. The optimization reduces execution time from 623us to 395us for specific input configurations (input:64k, output:1k, batch_size:1). The changes are focused on the Triton implementation at `vllm_ascend/ops/triton/linearnorm/split_qkv_tp_rmsnorm_rope.py`.

## Technical Significance
The optimization demonstrates effective Triton kernel tuning for Ascend NPU by improving the efficiency of the fused split QKV, RMS normalization, and RoPE operations. This fusion pattern is critical for transformer model inference performance, particularly during prefill where the kernel shows a 37% performance improvement. The optimization is important for models using tensor parallelism with attention mechanisms.

## Related
- `technique-operator-fusion`
- `technique-triton-optimization`