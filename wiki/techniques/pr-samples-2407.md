---
id: technique-pr-samples-2407
title: "PR Insight: Ascend/samples #2407"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - quantization
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2407"
---

# PR Insight: Ascend/samples #2407

**Title:** 添加Matmul常量化样例

## Overview
This PR adds matmul constant quantization samples, demonstrating how to perform matrix multiplication with quantized constant weights (often from pre-trained models). This is a key pattern for efficient inference where weights are quantized but activations remain higher precision.

## Technical Significance
Constant quantization is widely used in production inference to reduce memory bandwidth and accelerate compute. These samples show how to handle the format conversion and compute patterns for quantized matmul on Ascend hardware.

## Related
- `kernel-matmul-ascendc`, `technique-quantization`, `technique-format-conversion`