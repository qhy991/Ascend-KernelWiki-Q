---
id: technique-pr-samples-2477
title: "PR Insight: Ascend/samples #2477"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - quantization
  - hif8
  - fp8
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2477"
---

# PR Insight: Ascend/samples #2477

**Title:** 【AR20240408408475】hif8/fp8 quant sample

## Overview
This PR adds quantization samples for HiF8 and FP8 data types, which are 8-bit floating-point formats. HiF8 is Huawei's proprietary format while FP8 is a standardized format. Both are important for modern quantization schemes.

## Technical Significance
FP8 quantization is becoming increasingly important for large language model inference. Samples covering both HiF8 and FP8 help developers understand format-specific considerations and choose the right format for their use case.

## Related
- `technique-quantization`, `technique-format-conversion`