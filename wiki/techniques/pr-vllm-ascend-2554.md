---
id: technique-pr-vllm-ascend-2554
title: "PR Insight: vllm-project/vllm-ascend #2554"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - hccl-optimization
  - mtp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2554"
---

# PR Insight: vllm-project/vllm-ascend #2554

**Title:** [0.9.1][bugfix] Address abnormal VRAM increase in quantized models with floating-point MTP

## Overview
This PR fixes abnormal VRAM increase during mixed-precision inference with quantized models and floating-point MTP (Multi-Token Prediction). The issue was caused by `dist.all_to_all_single` creating extra HCCL communicators, leading to unnecessary buffer allocations that consumed more memory.

## Technical Significance
The fix involves adding a communicator parameter to `dist.all_to_all_single` in `vllm_ascend/quantization/w8a8_dynamic.py`. By passing the existing communicator from the vllm-ascend framework, all communication operations use a unified domain, preventing the creation of extra buffers and solving the VRAM issue. This optimization reduces memory pressure during quantized inference with MTP.

## Related
- `technique-hccl-optimization`
- `technique-quantization`