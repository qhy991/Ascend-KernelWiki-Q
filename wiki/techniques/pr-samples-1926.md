---
id: technique-pr-samples-1926
title: "PR Insight: Ascend/samples #1926"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - pytorch
  - qat
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1926"
---

# PR Insight: Ascend/samples #1926

**Title:** rename amct_pytorch/resnet-101/src/resnet-101_qat_op.py.

## Overview
This PR renames the ResNet-101 quantization-aware training operator file within the AMCT PyTorch samples. The rename likely improves consistency with naming conventions or reflects a reorganization of the quantization workflow code structure for better maintainability.

## Technical Significance
Quantization-aware training (QAT) is critical for achieving high accuracy with quantized models on Ascend hardware. The ResNet-101 QAT sample demonstrates how to integrate AMCT's quantization simulation into PyTorch training pipelines, enabling models to learn quantization-friendly weights for efficient deployment on Ascend910/910B.

## Related
- `technique-quantization`
- `kernel-resnet`