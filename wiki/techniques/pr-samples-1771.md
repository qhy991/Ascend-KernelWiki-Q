---
id: technique-pr-samples-1771
title: "PR Insight: Ascend/samples #1771"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - resnet
  - tensorflow
  - samples
  - model-download
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1771"
---

# PR Insight: Ascend/samples #1771

**Title:** 修改resnet50 v1模型文件链接，并更新sample中输出节点名称

## Overview
This PR updates the ResNet50 v1 model file download link and corrects the output node names in the sample code.

## Technical Significance
Keeping model download links current and ensuring correct output node names are both essential for samples to work reliably. ResNet50 is a widely used classification model, and maintaining accurate references helps developers successfully run inference benchmarks and applications.

## Related
- `wiki-technique-inference`
- `wiki-technique-model-conversion`