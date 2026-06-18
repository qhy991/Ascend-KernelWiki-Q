---
id: technique-pr-vllm-ascend-1920
title: "PR Insight: vllm-project/vllm-ascend #1920"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - topk
  - topp
  - fused-ops
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1920"
---

# PR Insight: vllm-project/vllm-ascend #1920

**Title:** [0.9.1][Perf] Use fused ops npu_top_k_top_p

## Overview
This PR uses the fused operation torch_npu.npu_top_k_top_p when both p and k parameters are not None, falling back to the original implementation otherwise. The fusion is automatically enabled when VLLM_ASCEND_ENABLE_TOPK_OPTIMIZE=1 and requires torch_npu>=2.5.1.post1.dev20250619.

## Technical Significance
Operator fusion for sampling operations. The npu_top_k_top_p operation combines top-k and top-p sampling into a single NPU kernel, reducing kernel launch overhead and improving sampling performance.

## Related
- `kernel-topk-ascendc`
- `technique-operator-fusion`
- `technique-sampling-optimization`