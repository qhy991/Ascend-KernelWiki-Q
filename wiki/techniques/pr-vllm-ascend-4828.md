---
id: technique-pr-vllm-ascend-4828
title: "PR Insight: vllm-project/vllm-ascend #4828"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseekv3
  - mlapo
  - w4a8
  - quantization
  - mla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4828"
---

# PR Insight: vllm-project/vllm-ascend #4828

**Title:** [Bugfix] Support for mlapo in deepseekv3.1 w4a8

## Overview
This PR adds support for the MLAPO operator in DeepSeekV3.1 with W4A8 quantization, extending the optimized MLA attention to work with 4-bit weight and 8-bit activation quantization.

## Technical Significance
Enables the use of the optimized MLAPO operator for W4A8-quantized DeepSeekV3.1 models, combining the computational efficiency of MLAPO with the memory savings of W4A8 quantization.

## Related
- `kernel-mlapo`
- `technique-mla`
- `kernel-deepseekv3`
- `technique-w4a8-quantization`