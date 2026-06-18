---
id: technique-pr-samples-2572
title: "PR Insight: Ascend/samples #2572"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - yolo
  - cmakelists
  - build-configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2572"
---

# PR Insight: Ascend/samples #2572

**Title:** update inference/modelInference/sampleYOLOV7/src/CMakeLists.txt.

## Overview
This PR updates the CMakeLists.txt configuration for the sampleYOLOV7 inference sample. The change modifies build settings, dependencies, or compilation flags for the YOLOV7 sample.

## Technical Significance
YOLO is a popular object detection model. Proper build configuration is essential for successful compilation and linking of inference samples. CMakeLists.txt management ensures samples can be built correctly across different environments.

## Related
- `kernel-attention-ascendc`
- `technique-pipeline-scheduling`