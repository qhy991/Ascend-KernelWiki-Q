---
id: technique-pr-vllm-ascend-9280
title: "PR Insight: vllm-project/vllm-ascend #9280"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascend950
  - eplb
  - mxfp
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9280"
---

# PR Insight: vllm-project/vllm-ascend #9280

**Title:** [Ascend950] [Feature]EPLB support W8A8_MXFP and W4A4_MXFP

## Overview
This PR adds support for W8A8_MXFP and W4A4_MXFP quantization formats to the EPLB (Expert Parameter Load Balancing) system on Ascend 950. The change is implemented in the vLLM adaptor layer, enabling EPLB to work with these mixed-precision floating-point quantization schemes.

## Technical Significance
MXFP (Mixed-Precision Floating Point) quantization provides better accuracy than integer quantization while still reducing memory bandwidth and storage requirements. Supporting these formats in EPLB enables efficient expert routing and parameter management for large MoE models with improved accuracy-performance tradeoffs.

## Related
- `technique-quantization`
- `kernel-moe`