---
id: technique-pr-mindspeed-2453
title: "PR Insight: Ascend/MindSpeed #2453"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - test
  - conv3d
  - depth-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2453"
---

# PR Insight: Ascend/MindSpeed #2453

**Title:** add ut for Conv3dDepthParallel

## Overview
This PR adds unit tests for Conv3dDepthParallel, which is a 3D convolution operation with depth parallelism. Conv3D is commonly used in video processing and 3D medical imaging models.

## Technical Significance
Validates the correctness of 3D convolution operations with depth-based parallelism on Ascend NPUs. Proper test coverage ensures that spatial and temporal features are correctly processed in 3D convolution layers.

## Related
- `technique-distributed-training`
- `technique-conv3d-ascendc`