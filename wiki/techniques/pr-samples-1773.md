---
id: technique-pr-samples-1773
title: "PR Insight: Ascend/samples #1773"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tensorflow
  - resnet
  - samples
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1773"
---

# PR Insight: Ascend/samples #1773

**Title:** 修改tensorflow的resnet50 v1模型输入节点名称

## Overview
This PR fixes the input node name for the ResNet50 v1 model in the TensorFlow samples, ensuring correct model graph parsing.

## Technical Significance
Accurate input/output node names are critical for model conversion and inference workflows. Node name mismatches can cause failures during model loading or incorrect input data routing, so fixing these issues ensures samples work correctly with the specified model architectures.

## Related
- `wiki-technique-inference`
- `wiki-technique-model-conversion`