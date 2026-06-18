---
id: technique-pr-samples-829
title: "PR Insight: Ascend/samples #829"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - image-processing
  - edvr
  - video-restoration
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/829"
---

# PR Insight: Ascend/samples #829

**Title:** add EDVR sample

## Overview
This PR adds a new sample for EDVR (Enhanced Deformable Convolution Video Restoration), a state-of-the-art model for video super-resolution and restoration tasks. The sample demonstrates how to deploy EDVR on Ascend NPU for video enhancement.

## Technical Significance
EDVR is an advanced video restoration model that uses deformable convolutions for high-quality video upscaling and enhancement. This sample shows how to deploy complex video processing models on Ascend, demonstrating the NPU's capability for handling video inference with temporal dependencies. It provides a reference for deploying video super-resolution and restoration models, which are important for high-quality video processing applications.

## Related
- EDVR video restoration on Ascend
- Video super-resolution models
- Deformable convolution deployment
- Video inference with temporal modeling