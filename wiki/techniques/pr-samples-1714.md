---
id: technique-pr-samples-1714
title: "PR Insight: Ascend/samples #1714"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolov7
  - object-detection
  - multi-input
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1714"
---

# PR Insight: Ascend/samples #1714

**Title:** 案例sampleYolov7MultiInput功能点新增

## Overview
This PR adds new functionality to the YOLOv7 multi-input sample case, demonstrating how to handle multiple input streams for object detection tasks on Ascend hardware.

## Technical Significance
Multi-input object detection scenarios (e.g., multi-camera processing) are common in industrial applications. This sample shows how to structure inference pipelines to handle concurrent input streams efficiently on Ascend NPUs.

## Related
- kernel-yolov7
- technique-object-detection