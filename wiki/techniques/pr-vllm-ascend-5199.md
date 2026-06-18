---
id: technique-pr-vllm-ascend-5199
title: "PR Insight: vllm-project/vllm-ascend #5199"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - nz-format
  - quantization
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5199"
---

# PR Insight: vllm-project/vllm-ascend #5199

**Title:** [bugfix] fix w8a8dynamic fused_moe trans nz

## Overview
This PR fixes W8A8 dynamic quantized fused MoE by forcing NZ format transformation for w13_weight and w2_weight tensors. The fix addresses a limitation where `torch_npu.npu_grouped_matmul_swiglu_quant` only supports weight in NZ format.

## Technical Significance
NZ format is optimized for MLU memory layout and critical for efficient group matrix multiplication operations on Ascend NPUs. Ensuring proper format transformation for quantized MoE weights maintains performance for W8A8 dynamic quantization workloads.

## Related
- technique-nz-tiling
- technique-quantization
- technique-moe