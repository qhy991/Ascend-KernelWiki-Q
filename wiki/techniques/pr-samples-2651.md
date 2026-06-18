---
id: technique-pr-samples-2651
title: "PR Insight: Ascend/samples #2651"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - quantization
  - fp8
  - hif8
  - weight-only
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2651"
---

# PR Insight: Ascend/samples #2651

**Title:** 【AR20241227785719】fp8/hi8 weight only

## Overview
This PR adds samples for FP8/Hi8 weight-only quantization, where weights are quantized to 8-bit but activations remain in higher precision. Weight-only quantization balances memory savings and accuracy.

## Technical Significance
Weight-only quantization is widely used in production inference. Samples demonstrate how to implement this pattern on Ascend, handling weight loading, format conversion, and computation correctly.

## Related
- `technique-quantization`, `technique-format-conversion`