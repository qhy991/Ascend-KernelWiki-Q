---
id: technique-pr-samples-1149
title: "PR Insight: Ascend/samples #1149"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpege
  - preprocessing
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1149"
---

# PR Insight: Ascend/samples #1149

**Title:** for jpege, add input arguments for handle any file and modify the output name to record the width and height.

## Overview
This PR enhances the JPEG encoder (JPEGE) sample by adding input arguments to handle any file type and modifying output filenames to include image dimensions (width and height). This makes the sample more flexible and provides better output organization.

## Technical Significance
Flexible input handling allows JPEGE to process various image formats, while dimension-aware output naming improves file organization and debugging. This enhancement is useful for batch processing workflows where tracking image dimensions helps verify preprocessing steps before feeding images to neural networks.

## Related
- JPEG encoder (JPEGE) implementation
- Image preprocessing pipelines
- Batch processing workflows
- File naming conventions