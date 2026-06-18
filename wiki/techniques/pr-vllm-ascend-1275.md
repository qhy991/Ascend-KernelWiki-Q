---
id: technique-pr-vllm-ascend-1275
title: "PR Insight: vllm-project/vllm-ascend #1275"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - w4a8
  - qwen3
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1275"
---

# PR Insight: vllm-project/vllm-ascend #1275

**Title:** [0.9.1][Feature] Support Qwen3 W4A8 quantization

## Overview
This PR adds W4A8 (4-bit weight, 8-bit activation) quantization support for Qwen3 models on Ascend NPU. It extends the quantization framework with new W4A8 dynamic quantization implementation and configuration handling.

## Technical Significance
Enables memory-efficient inference of Qwen3 models through W4A8 quantization, reducing memory footprint by ~50% compared to FP16. The implementation adds `w4a8_dynamic.py` quantization operator, updates quantization configuration, and provides test coverage for multi-card deployments. This extends the existing W8A8 quantization infrastructure to support lower-bit weights while maintaining accuracy through dynamic activation quantization.

## Related
- `technique-w4a8-quantization`
- `technique-w8a8-quantization`
- `kernel-qwen3`