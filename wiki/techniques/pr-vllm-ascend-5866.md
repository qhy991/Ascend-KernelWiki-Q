---
id: technique-pr-vllm-ascend-5866
title: "PR Insight: vllm-project/vllm-ascend #5866"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-ffn
  - ascenC
  - feature
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5866"
---

# PR Insight: vllm-project/vllm-ascend #5866

**Title:** add dispath_ffn_combine_bf16

## Overview
This PR adds a new AscendC operator `dispatch_ffn_combine_bf16` for MoE FFN dispatch and combination with bfloat16 precision. The operator handles expert routing, token distribution to experts, FFN computation, and result aggregation for MoE models.

## Technical Significance
The new operator provides optimized MoE FFN support with bfloat16 precision, which can improve performance and reduce memory usage compared to fp32 or fp16 implementations. The operator includes comprehensive components: host-side CMakeLists, ACLNN interface, tiling logic, kernel implementation with multistage workspace support, MoE v2 routing, sorting algorithms, and utility functions for block epilogues, memory transfers, and HCCL communication. It also includes e2e tests for multicard A3 deployments.

## Related
- `technique-moe-dispatch`, `technique-ascendc`, `technique-fusion`