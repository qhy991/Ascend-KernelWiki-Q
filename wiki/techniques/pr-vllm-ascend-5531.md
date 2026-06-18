---
id: technique-pr-vllm-ascend-5531
title: "PR Insight: vllm-project/vllm-ascend #5531"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - fp16
  - bf16
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5531"
---

# PR Insight: vllm-project/vllm-ascend #5531

**Title:** [EPLB][Bugfix] EPLB support fp/bf16

## Overview
This PR adds FP16 and BF16 dtype support for EPLB (Expert Parallel Load Balancing), extending compatibility beyond W8A8 dynamic quantization. The implementation modifies the VLLM adaptor and Fused MoE operations to handle floating-point dtypes while maintaining accuracy across quantization modes.

## Technical Significance
Enabling EPLB with FP16/BF16 dtypes provides flexibility for users who prefer floating-point precision over quantization. The fix maintains EPLB accuracy across different dtype configurations, ensuring that expert parallel load balancing benefits are available for both quantized and floating-point MoE inference scenarios.

## Related
- `pattern-moe` (MoE patterns and operations)
- `technique-expert-parallelism` (Expert parallel load balancing)
- `kernel-quantization` (Multi-dtype support)