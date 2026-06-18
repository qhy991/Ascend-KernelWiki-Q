---
id: technique-pr-samples-655
title: "PR Insight: Ascend/samples #655"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolo
  - object-detection
  - multithreading
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/655"
---

# PR Insight: Ascend/samples #655

**Title:** YOLOV3_coco_detection_4_thread

## Overview
This PR adds or modifies a YOLOV3 COCO object detection sample that uses 4 threads for parallel processing. The multithreaded implementation improves throughput by leveraging multiple CPU threads.

## Technical Significance
Implementing multithreaded YOLOV3 demonstrates how to achieve higher throughput on Ascend hardware by parallelizing preprocessing and postprocessing across multiple threads. This is important for real-time applications requiring high FPS object detection.

## Related
- N/A (multithreading)