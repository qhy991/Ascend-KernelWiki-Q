---
id: technique-pr-samples-929
title: "PR Insight: Ascend/samples #929"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - camera
  - preprocessing
  - migration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/929"
---

# PR Insight: Ascend/samples #929

**Title:** opencv to atlas_camera

## Overview
Migrates samples from using OpenCV camera APIs to using Atlas camera APIs, likely for better integration with Ascend hardware preprocessing pipelines.

## Technical Significance
Using native camera APIs instead of OpenCV can improve performance by reducing data copies and enabling direct hardware streaming into DVPP buffers.

## Related
- `technique-dvpp-optimization` / `technique-preprocessing`
