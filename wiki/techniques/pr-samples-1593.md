---
id: technique-pr-samples-1593
title: "PR Insight: Ascend/samples #1593"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - dvpp
  - python
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1593"
---

# PR Insight: Ascend/samples #1593

**Title:** sampleResnetDVPP.py案例修改

## Overview
This PR modifies the ResNet sample code that uses DVPP (Digital Vision Pre-Processing) for hardware-accelerated image preprocessing. ResNet is a deep residual network commonly used for image classification.

## Technical Significance
DVPP integration is crucial for achieving high-throughput inference by offloading image decode, resize, and normalization to dedicated hardware. The sample modifications likely improve DVPP pipeline efficiency, fix memory management issues, or enhance error handling in the preprocessing stage before model inference.

## Related
- `kernel-resnet`
- `technique-dvpp`
- `technique-pipeline-scheduling`
- `hw-unified-buffer`