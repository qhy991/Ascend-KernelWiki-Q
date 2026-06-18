---
id: technique-pr-samples-2652
title: "PR Insight: Ascend/samples #2652"
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
  - npu
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2652"
---

# PR Insight: Ascend/samples #2652

**Title:** 【AR20241227785719】fp8/hi8 weight only npu

## Overview
This PR adds NPU-specific samples for FP8/Hi8 weight-only quantization (from PR #2651). NPU-specific optimizations may include format support, data movement patterns, or hardware-specific kernels.

## Technical Significance
NPU-specific samples demonstrate how to leverage Ascend hardware features for quantized inference. These optimizations are important for achieving maximum performance on Ascend NPUs.

## Related
- `technique-quantization`, `technique-format-conversion`, `hw-cube-unit`