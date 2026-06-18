---
id: technique-pr-samples-795
title: "PR Insight: Ascend/samples #795"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - bugfix
  - crowd-counting
  - computer-vision
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/795"
---

# PR Insight: Ascend/samples #795

**Title:** fixed crowd_count

## Overview
This PR fixes issues in the crowd counting sample. Crowd counting is a computer vision task that estimates the number of people in an image, typically using density estimation models.

## Technical Significance
Crowd counting is an important application for surveillance and safety monitoring. This fix ensures that the crowd counting sample works correctly on Ascend NPU, demonstrating deployment of density estimation models. The fix likely addresses accuracy issues, runtime errors, or data preprocessing problems specific to crowd counting workflows.

## Related
- Crowd counting inference on Ascend
- Density estimation models
- Computer vision for people counting