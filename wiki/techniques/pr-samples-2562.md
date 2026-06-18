---
id: technique-pr-samples-2562
title: "PR Insight: Ascend/samples #2562"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolo
  - multi-input
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2562"
---

# PR Insight: Ascend/samples #2562

**Title:** sampleYOLOV7MultiInput修改

## Overview
This PR modifies the sampleYOLOV7MultiInput sample. The changes update the multi-input YOLOV7 example to reflect current best practices or fix issues in the multi-input processing pipeline.

## Technical Significance
Multi-input processing is important for complex inference scenarios like video processing or multi-stream applications. YOLOV7 with multiple inputs demonstrates how to handle concurrent inference workloads efficiently.

## Related
- `kernel-attention-ascendc`
- `technique-pipeline-scheduling`