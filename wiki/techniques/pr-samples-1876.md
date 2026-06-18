---
id: technique-pr-samples-1876
title: "PR Insight: Ascend/samples #1876"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - caffe
  - resnet
  - quantization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1876"
---

# PR Insight: Ascend/samples #1876

**Title:** amct_caffe resnet50使用自行上传模型，并修改下载模型脚本

## Overview
This PR updates the AMCT Caffe ResNet50 sample to use self-uploaded models instead of automatically downloading them, and modifies the model download script accordingly. The change improves flexibility by allowing developers to use their own ResNet50 models for quantization workflows.

## Technical Significance
Model upload flexibility is important for quantization workflows, as developers often need to quantize custom models rather than standard pretrained models. This update demonstrates how to adapt AMCT workflows for user-provided models in Caffe, ensuring the quantization pipeline works correctly with Ascend910/910B for a variety of ResNet50 model variants.

## Related
- `technique-quantization`
- `kernel-resnet`
- `pattern-model-loading`