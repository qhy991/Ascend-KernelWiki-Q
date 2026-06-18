---
id: technique-pr-vllm-ascend-9365
title: "PR Insight: vllm-project/vllm-ascend #9365"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascend950
  - a5
  - mxfp4
  - quantization
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9365"
---

# PR Insight: vllm-project/vllm-ascend #9365

**Title:** [Ascend950][Feature]enable mc2 dispatch MXFP4 quantization in A5

## Overview
This PR enables MXFP4 quantization for the mc2 dispatch operator in A5 hardware by updating the MoE stage parameters and token dispatcher. The change allows the MoE dispatch operation to use ultra-low precision floating-point quantization for maximum memory efficiency.

## Technical Significance
MXFP4 provides the most aggressive memory reduction among MXFP formats while maintaining acceptable accuracy for many workloads. Enabling this for MoE dispatch significantly reduces memory bandwidth requirements for large MoE models, which is critical for serving models with many experts efficiently.

## Related
- `kernel-moe`
- `technique-quantization`