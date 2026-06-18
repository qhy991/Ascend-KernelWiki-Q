---
id: technique-pr-samples-1921
title: "PR Insight: Ascend/samples #1921"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - resnet
  - retrain
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1921"
---

# PR Insight: Ascend/samples #1921

**Title:** 修改resnet50 retrain脚本中拼写问题

## Overview
This PR fixes a spelling error in the ResNet50 retraining script within the AMCT samples. The correction ensures that variable names, file paths, or configuration parameters are correctly spelled, preventing runtime errors or misconfiguration in the quantization-aware retraining workflow.

## Technical Significance
Typographical errors in training scripts can cause subtle bugs that are difficult to diagnose, especially in complex quantization workflows. Fixing these issues improves the reliability of the ResNet50 retrain sample, ensuring developers can successfully run post-quantization fine-tuning for Ascend910/910B deployment without encountering cryptic errors.

## Related
- `technique-quantization`
- `kernel-resnet`
- `pattern-script-correctness`