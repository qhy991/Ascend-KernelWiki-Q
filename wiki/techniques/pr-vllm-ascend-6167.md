---
id: technique-pr-vllm-ascend-6167
title: "PR Insight: vllm-project/vllm-ascend #6167"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sp
  - tp
  - hccl-optimization
  - torch-npu
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6167"
---

# PR Insight: vllm-project/vllm-ascend #6167

**Title:** [0.13.0][B
ugFix] Avoided a bug of `torch_npu.npu_mm_reduce_scatter_base` when sp size >= 16

## Overview
This PR fixes a bug where `torch_npu.npu_mm_reduce_scatter_base` raises an exception when sequence parallelism (SP) is enabled with tensor parallelism size (TP) >= 16. The fix disables this operator when TP >= 16 by checking the tensor parallel size conditionally.

## Technical Significance
`torch_npu.npu.mm_reduce_scatter_base` is a fused matrix multiplication and reduce-scatter operator that combines GEMM with communication. The operator has limitations when the number of parallel devices reaches 16, causing exceptions. The fix gracefully falls back to separate GEMM and communication operations at this scale, maintaining functionality while avoiding the operator's limitations.

## Related
- `technique-sp`, `technique-tp`, `technique-hccl-optimization`, `technique-operator-fusion`