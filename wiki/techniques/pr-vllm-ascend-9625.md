---
id: technique-pr-vllm-ascend-9625
title: "PR Insight: vllm-project/vllm-ascend #9625"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - w4a8
  - nz-format
  - moe
  - performance
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9625"
---

# PR Insight: vllm-project/vllm-ascend #9625

**Title:** [Performance] Support NZ format for w4a8 MoE of compressed tensor

## Overview
This PR adds support for NZ format (a specialized memory layout) for W4A8 MoE operations with compressed tensors. The implementation updates the W4A8 quantization method and adds corresponding tests.

## Technical Significance
NZ format provides better memory access patterns for certain operations by optimizing data layout for the Ascend hardware's memory hierarchy. Supporting NZ format for compressed W4A8 MoE tensors improves memory bandwidth utilization and overall inference performance for quantized MoE models.

## Related
- `kernel-moe`
- `technique-nz-tiling`
- `technique-quantization`
- `hw-cube-unit`