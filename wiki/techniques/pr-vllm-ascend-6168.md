---
id: technique-pr-vllm-ascend-6168
title: "PR Insight: vllm-project/vllm-ascend #6168"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/6168"
---

# PR Insight: vllm-project/vllm-ascend #6168

**Title:** [main][BugFix] Avoided a bug of `torch_npu.npu_mm_reduce_scatter_base` when sp size >= 16

## Overview
This PR fixes a bug in the main branch where `torch_npu.npu_mm_reduce_scatter_base` raises an exception when sequence parallelism (SP) is enabled with tensor parallelism size (TP) >= 16. The fix adds a conditional check to disable this operator when TP >= 16.

## Technical Significance
This is the main branch version of the fix for PR #6167. The `torch_npu.npu.mm_reduce_scatter_base` operator combines matrix multiplication with reduce-scatter communication but has limitations at TP >= 16. The fix ensures graceful fallback to separate operations at this scale, maintaining functionality while avoiding the operator's limitations in large-scale distributed inference.

## Related
- `technique-sp`, `technique-tp`, `technique-hccl-optimization`, `technique-operator-fusion`