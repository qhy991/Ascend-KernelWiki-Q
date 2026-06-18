---
id: technique-pr-catlass-93
title: "PR Insight: Ascend/catlass #93"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/93"
---

# PR Insight: Ascend/catlass #93

**Title:** 修复quantmatmul在调整epilogueTileShape时的精度错误

## Overview
This PR fixes a numerical precision error in quantized matmul operations when adjusting the epilogue tile shape configuration. The fix ensures correctness for quantized matrix multiplication on Ascend hardware.

## Technical Significance
Quantized matmul is critical for efficient inference with reduced memory bandwidth and compute requirements. Precision errors can accumulate and degrade model accuracy, making this fix essential for reliable low-precision inference on Ascend NPUs.

## Related
- `kernel-matmul-ascendc`
- `technique-quantization`