---
id: technique-pr-samples-1809
title: "PR Insight: Ascend/samples #1809"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - resnet
  - dvpp
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1809"
---

# PR Insight: Ascend/samples #1809

**Title:** 案例sampleResnetDVPP更新结构

## Overview
This PR updates the structure of the sampleResnetDVPP sample, which performs ResNet inference with DVPP preprocessing.

## Technical Significance
Structural updates improve sample organization and make the code easier to understand and modify. The ResNet DVPP sample demonstrates how to integrate DVPP hardware acceleration with neural network inference, showing the complete pipeline from image preprocessing to model execution.

## Related
- `wiki-technique-inference`
- `hw-dvpp`