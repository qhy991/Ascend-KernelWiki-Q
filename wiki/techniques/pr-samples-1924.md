---
id: technique-pr-samples-1924
title: "PR Insight: Ascend/samples #1924"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - retrain
  - amct
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1924"
---

# PR Insight: Ascend/samples #1924

**Title:** retreat change for resnet50 retrain

## Overview
This PR reverts a previous change to the ResNet50 retraining workflow within the AMCT samples. The reversion likely indicates that the original change introduced issues or was no longer needed after a different approach was found for the ResNet50 retrain process in the quantization workflow.

## Technical Significance
Post-quantization retraining is a common technique to recover accuracy lost during quantization. The ResNet50 retrain sample demonstrates the AMCT workflow for fine-tuning quantized models, and careful management of changes ensures that the reference implementation remains stable and correct for Ascend910/910B deployment.

## Related
- `technique-quantization`
- `kernel-resnet`
- `pattern-model-retraining`