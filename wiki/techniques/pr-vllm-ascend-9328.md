---
id: technique-pr-vllm-ascend-9328
title: "PR Insight: vllm-project/vllm-ascend #9328"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascend950
  - a5
  - eplb
  - mxfp8
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9328"
---

# PR Insight: vllm-project/vllm-ascend #9328

**Title:** [Ascend950][Feature][quant] enable mc2 combine mxfp8 quant in A5

## Overview
This PR enables MXFP8 quantization for the mc2 (MoE combine) operator in A5 hardware by updating the EPLB token dispatcher and MoE stage parameters. The change allows the MoE combine operation to use mixed-precision floating-point quantization for improved accuracy and memory efficiency.

## Technical Significance
MXFP8 quantization provides better accuracy than traditional integer quantization while still reducing memory bandwidth. Enabling this for the MoE combine operator improves the accuracy-performance tradeoff for large MoE models on A5 hardware, which is critical for deploying state-of-the-art language models.

## Related
- `kernel-moe`
- `technique-quantization`