---
id: technique-pr-samples-617
title: "PR Insight: Ascend/samples #617"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - pytorch
  - quantization
  - calibration
  - retrain
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/617"
---

# PR Insight: Ascend/samples #617

**Title:** 添加AMCT PyTorch calibration&retrain用例

## Overview
This PR adds AMCT PyTorch use cases covering both calibration and retrain workflows for quantization. Calibration determines optimal quantization parameters, while retrain fine-tunes the model to recover accuracy lost during quantization.

## Technical Significance
The calibration and retrain workflow is critical for achieving high accuracy in quantized models. Having comprehensive samples for PyTorch enables users to apply advanced quantization techniques effectively, particularly important for production deployments where accuracy cannot be sacrificed.

## Related
- technique-operator-fusion
- Quantization calibration
- Model retraining
- AMCT toolkit
- PyTorch quantization