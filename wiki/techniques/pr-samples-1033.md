---
id: technique-pr-samples-1033
title: "PR Insight: Ascend/samples #1033"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolov3
  - detection
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1033"
---

# PR Insight: Ascend/samples #1033

**Title:** add sample  YOLOV3_carColor_sample

## Overview
This PR adds a new YOLOV3 car color detection sample to the Ascend samples repository. The sample demonstrates how to deploy YOLOV3 object detection combined with car color classification on Ascend hardware.

## Technical Significance
Expands the sample library for detection + classification use cases, showing how to chain multiple models (detection + classification) on Ascend NPUs for automotive/traffic analysis scenarios.

## Related
- `kernel-detection` / `technique-inference-optimization`
