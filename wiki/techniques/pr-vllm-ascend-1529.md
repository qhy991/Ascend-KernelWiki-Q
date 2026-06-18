---
id: technique-pr-vllm-ascend-1529
title: "PR Insight: vllm-project/vllm-ascend #1529"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - w8a8
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1529"
---

# PR Insight: vllm-project/vllm-ascend #1529

**Title:** Fix W8A8 fused moe bug

## Overview
This PR fixes bugs in W8A8 quantized fused MoE operations, ensuring correct numerical behavior for quantized MoE inference.

## Technical Significance
Corrects numerical precision and correctness issues in W8A8 MoE that caused incorrect expert selection and computation. The fix spans attention, quantization configuration, and model runner components, ensuring quantized MoE maintains accuracy parity with FP16 baseline.

## Related
- `kernel-moe`
- `technique-w8a8-quantization`