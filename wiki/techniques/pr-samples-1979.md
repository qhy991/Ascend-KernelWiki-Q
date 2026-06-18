---
id: technique-pr-samples-1979
title: "PR Insight: Ascend/samples #1979"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - inference
  - yolov7
  - cpp
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1979"
---

# PR Insight: Ascend/samples #1979

**Title:** 【轻量级 PR】：update inference/modelInference/sampleYOLOV7MultiInput/src/main.cpp.

## Overview
This PR updates the main.cpp source file for the YOLOV7 multi-input inference sample. The changes are lightweight updates to the C++ inference code.

## Technical Significance
YOLOV7 multi-input samples demonstrate object detection with multiple input sources. Code updates may improve input handling, model preprocessing, or result post-processing, helping developers understand how to implement multi-stream inference on Ascend hardware.

## Related
- `technique-ascendc`