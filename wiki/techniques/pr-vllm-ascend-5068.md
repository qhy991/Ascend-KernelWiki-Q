---
id: technique-pr-vllm-ascend-5068
title: "PR Insight: vllm-project/vllm-ascend #5068"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - nz-format
  - format-conversion
  - fp32
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5068"
---

# PR Insight: vllm-project/vllm-ascend #5068

**Title:** [bugfix] fix fp32 trans nz

## Overview
This PR fixes a format conversion error by disabling NZ (Non-Zero) format transposition for FP32 data types. The fix prevents NZ transformation errors that occur when attempting to apply the NZ format to FP32 tensors in vLLM-Ascend.

## Technical Significance
The NZ format is optimized for MLU (MindSpore Learning Unit) memory layout but is not compatible with FP32 data. This fix ensures correct data format handling by preventing invalid NZ conversions for FP32 tensors, maintaining proper memory alignment and computational efficiency on Ascend NPUs.

## Related
- technique-nz-tiling
- technique-format-conversion
- hw-cube-unit