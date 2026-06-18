---
id: technique-pr-samples-1648
title: "PR Insight: Ascend/samples #1648"
type: wiki-technique
architectures:
  - ascend310p
  - ascend310p
tags:
  - samples
  - 310b
  - image-colorization
  - porting
  - computer-vision
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1648"
---

# PR Insight: Ascend/samples #1648

**Title:** 310B样例迁移-黑白图像上色

## Overview
This PR ports the black-and-white image colorization sample to the Ascend 310B platform, adapting the generative vision application for edge deployment.

## Technical Significance
Image colorization is a computer vision task that adds color to grayscale images, commonly used for photo restoration and enhancement. Porting to 310B demonstrates how to optimize generative models for edge devices, handling the memory and compute constraints of the 310B architecture.

## Related
- hw-ascend310p
- technique-generative-models