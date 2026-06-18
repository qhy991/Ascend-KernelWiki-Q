---
id: technique-pr-vllm-ascend-7090
title: "PR Insight: vllm-project/vllm-ascend #7090"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w4a8
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7090"
---

# PR Insight: vllm-project/vllm-ascend #7090

**Title:** [bugdix] The problem that the w4a8 weight fails to be loaded when the EP is not enabled is resolved.

## Overview
Fixes a bug where MoE models fail to load W4A8 quantized weights when Expert Parallelism (EP) is not enabled. The fix ensures that parameters `["weight_scale_second", "weight_offset_second", "scale_bias"]` are parsed in per-group mode regardless of other conditions.

## Technical Significance
Enables W4A8 quantized weight loading for MoE models in non-EP configurations by fixing per-group parameter parsing. This allows users to leverage W4A8 quantization benefits even without expert parallelism enabled.

## Related
- `technique-quantization-w4a8`, `technique-moe`, `technique-weight-loading`, `technique-per-group-quantization`