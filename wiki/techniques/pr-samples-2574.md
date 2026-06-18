---
id: technique-pr-samples-2574
title: "PR Insight: Ascend/samples #2574"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - quantization
  - adaround
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2574"
---

# PR Insight: Ascend/samples #2574

**Title:** 【AR20250106997736】 adaround quant sample

## Overview
This PR adds samples for AdaRound quantization, which is a learned quantization method that rounds weights adaptively to minimize quantization error. AdaRound often produces better accuracy than traditional rounding schemes.

## Technical Significance
AdaRound is important for production quantization where accuracy must be preserved. Samples demonstrate how to implement AdaRound workflows on Ascend hardware.

## Related
- `technique-quantization`, `technique-format-conversion`