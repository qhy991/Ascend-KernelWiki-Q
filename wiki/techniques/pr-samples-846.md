---
id: technique-pr-samples-846
title: "PR Insight: Ascend/samples #846"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - image-processing
  - super-resolution
  - colorization
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/846"
---

# PR Insight: Ascend/samples #846

**Title:** Add colorization_and_super_resolution

## Overview
This PR adds a new sample for image colorization and super resolution. The sample demonstrates how to use Ascend NPU inference to perform both colorization of grayscale images and upscaling of low-resolution images.

## Technical Significance
Image colorization and super resolution are classic computer vision tasks that showcase NPU inference capabilities. This sample demonstrates end-to-end inference pipelines on Ascend, including data preprocessing, model execution, and post-processing. It likely uses convolutional neural networks optimized for Ascend, showing how to deploy advanced vision models on NPU hardware.

## Related
- Image colorization models on Ascend
- Super resolution inference workflows
- Computer vision pipeline patterns
- Image preprocessing and postprocessing