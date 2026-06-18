---
id: technique-pr-samples-837
title: "PR Insight: Ascend/samples #837"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - object-detection
  - mask-rcnn
  - inpainting
  - computer-vision
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/837"
---

# PR Insight: Ascend/samples #837

**Title:** add mask_rcnn_image_inpainting

## Overview
This PR adds a new sample for Mask R-CNN image inpainting. The sample combines object detection, segmentation, and image inpainting to demonstrate advanced computer vision workflows on Ascend NPU.

## Technical Significance
Mask R-CNN is a state-of-the-art model for instance segmentation, and combining it with inpainting demonstrates complex multi-stage vision pipelines. This sample shows how to chain multiple vision operations on Ascend: first detecting and segmenting objects with Mask R-CNN, then applying inpainting to fill or modify regions. This showcases the NPU's ability to handle sophisticated computer vision tasks beyond simple inference.

## Related
- Mask R-CNN inference on Ascend
- Instance segmentation workflows
- Image inpainting techniques
- Multi-stage vision pipelines