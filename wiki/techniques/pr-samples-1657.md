---
id: technique-pr-samples-1657
title: "PR Insight: Ascend/samples #1657"
type: wiki-technique
architectures:
  - ascend310p
  - ascend310p
tags:
  - samples
  - 310b
  - image-dehazing
  - porting
  - computer-vision
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1657"
---

# PR Insight: Ascend/samples #1657

**Title:** 310B样例迁移-图像去雾

## Overview
This PR ports the image dehazing sample to the Ascend 310B platform, adapting the computer vision application for edge deployment.

## Technical Significance
Image dehazing improves visibility in foggy conditions, useful for autonomous driving and outdoor monitoring. Porting to 310B demonstrates how to optimize computer vision models for edge devices with limited compute resources, including quantization, pruning, and latency optimization.

## Related
- wiki-hardware-ascend310p
- technique-image-enhancement