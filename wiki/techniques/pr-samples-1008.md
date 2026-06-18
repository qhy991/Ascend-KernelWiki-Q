---
id: technique-pr-samples-1008
title: "PR Insight: Ascend/samples #1008"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolov3
  - amct
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1008"
---

# PR Insight: Ascend/samples #1008

**Title:** 修复AMCT sample yolov3模型跳转

## Overview
Fixes an issue in the AMCT YOLOV3 sample where model execution jumps or skips steps, likely causing incorrect inference results.

## Technical Significance
Ensures correct execution flow in the AMCT-compressed YOLOV3 sample, which is critical for detection accuracy after quantization or compression.

## Related
- `technique-detection` / `technique-quantization` / `kernel-yolov3`
