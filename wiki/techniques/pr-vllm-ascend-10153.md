---
id: technique-pr-vllm-ascend-10153
title: "PR Insight: vllm-project/vllm-ascend #10153"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - mxfp
  - w4a8
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10153"
---

# PR Insight: vllm-project/vllm-ascend #10153

**Title:** [BugFix]fix w4a8 mxfp quantization in shared experts

## Overview
This PR fixes W4A8 MXFP quantization issues in shared experts components of MoE models. The quantization was not working correctly for shared expert weights, causing precision problems.

## Technical Significance
Fixes W4A8 MXFP quantization for MoE shared experts, ensuring that quantization works correctly for both shared and routed experts. Improves quantization accuracy and performance for MoE models using W4A8 MXFP quantization.

## Related
- `technique-quantization`, `technique-moe`, `technique-mxfp8`, `kernel-matmul`