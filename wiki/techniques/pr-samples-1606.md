---
id: technique-pr-samples-1606
title: "PR Insight: Ascend/samples #1606"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - mmdeploy
  - resnet
  - faster-rcnn
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1606"
---

# PR Insight: Ascend/samples #1606

**Title:** 【外部平台适配MMdeploy】新增mmdeploy推理案例/resnet50/faster-rcnn

## Overview
This PR adds MMDeploy inference samples for ResNet50 and Faster R-CNN models, enabling external platform adaptation. MMDeploy is a model deployment toolkit for OpenMMLab models.

## Technical Significance
MMDeploy integration demonstrates cross-platform model deployment patterns on Ascend. ResNet50 (classification) and Faster R-CNN (object detection) represent two fundamental vision task types, and these samples show how to convert and deploy OpenMMLab models on Ascend NPUs with proper operator mapping and runtime configuration.

## Related
- `kernel-resnet`
- `kernel-faster-rcnn`
- `technique-model-deployment`
- `technique-operator-mapping`