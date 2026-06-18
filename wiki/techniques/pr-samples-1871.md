---
id: technique-pr-samples-1871
title: "PR Insight: Ascend/samples #1871"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - tensorflow
  - resnet
  - model-download
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1871"
---

# PR Insight: Ascend/samples #1871

**Title:** DTS2023100907427：update tf resnet model download link

## Overview
This PR updates the TensorFlow ResNet model download link in response to defect ticket DTS2023100907427. The change fixes a broken or deprecated model download URL, ensuring the ResNet sample can successfully download the required pretrained model for inference or quantization workflows.

## Technical Significance
Model download links frequently change as model repositories reorganize or deprecate old versions. Keeping download URLs current is essential for sample code to work out-of-the-box, preventing user frustration and ensuring developers can run ResNet inference on Ascend910/910B without manual model acquisition.

## Related
- `kernel-resnet`
- `pattern-model-download`