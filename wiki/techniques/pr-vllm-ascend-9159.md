---
id: technique-pr-vllm-ascend-9159
title: "PR Insight: vllm-project/vllm-ascend #9159"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - mxfp8
  - bugfix
  - weight-scale
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9159"
---

# PR Insight: vllm-project/vllm-ascend #9159

**Title:** [Ascend950][BugFix] Fix w8a8_mxfp8 weight_scale group count: use cdiv for non-divisible input_size

## Overview
This PR fixes a bug in `AscendW8A8MXFP8DynamicLinearMethod.apply_weights` where the weight_scale group count was computed using integer floor division (`input_size // self.group_size`). When `input_size` is not divisible by `group_size` (e.g., Kimi-K2.5 with k_dim=4304 and group_size=32), one group would be missing, causing partial shape truncation of the weight_scale tensor and inference errors.

## Technical Significance
The fix replaces floor division with `vllm.utils.math_utils.cdiv(input_size, self.group_size)` to ensure proper rounding up, preventing missing groups and maintaining correct tensor shapes. This is critical for W8A8 MXFP8 quantization accuracy, particularly for models with input dimensions that are not evenly divisible by the group_size.

## Related
- `kernel-quantization-ascendc`, `technique-quantization`, `kernel-matmul-ascendc`