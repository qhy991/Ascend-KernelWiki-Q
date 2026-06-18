---
id: technique-pr-samples-2623
title: "PR Insight: Ascend/samples #2623"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - quantization
  - mxfp4
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2623"
---

# PR Insight: Ascend/samples #2623

**Title:** [AR20250121353425]mxfp4 quant sample

## Overview
This PR adds quantization samples for MXFP4, a 4-bit floating-point format. 4-bit formats offer even greater memory savings than FP8 but require careful handling to maintain accuracy.

## Technical Significance
Ultra-low-bit quantization (4-bit) is an active research area for extreme model compression. Samples provide practical guidance for implementing MXFP4 on Ascend hardware.

## Related
- `technique-quantization`, `technique-format-conversion`