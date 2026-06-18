---
id: technique-pr-vllm-ascend-6730
title: "PR Insight: vllm-project/vllm-ascend #6730"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - split-qkv-rmsnorm-mrope
  - fusion
  - triton
  - qwen3.5
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6730"
---

# PR Insight: vllm-project/vllm-ascend #6730

**Title:** [OPS]add split_qkv_rmsnorm_mrope ops

## Overview
This PR adds split_qkv_rmsnorm_mrope kernel with interleaved support for Qwen3.5 and Qwen3-VL models. The fused operation combines QKV splitting, RMS normalization, and multi-resolution positional encoding (mRoPE) for improved performance.

## Technical Significance
Enables efficient inference for Qwen3.5 and Qwen3-VL through advanced operator fusion. The interleaved mRoPE support provides better hardware utilization and reduced memory traffic compared to separate operations.

## Related
- `kernel-attention`
- `technique-operator-fusion`