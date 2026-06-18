---
id: technique-pr-samples-686
title: "PR Insight: Ascend/samples #686"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - quantization
  - pytorch
  - onnx
  - calibration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/686"
---

# PR Insight: Ascend/samples #686

**Title:** amct onnx pytorch auto calibration sample

## Overview
This PR adds an AMCT (Ascend Model Compression Toolkit) auto calibration sample that supports both ONNX and PyTorch models. Auto calibration is a quantization technique that automatically determines optimal scaling factors without requiring labeled calibration data.

## Technical Significance
Demonstrates advanced quantization workflows using AMCT's auto calibration feature, which simplifies the model compression process by eliminating the need for manually curated calibration datasets. This is particularly useful for production deployment scenarios where calibration data availability may be limited.

## Related
- technique-operator-fusion
- Quantization techniques
- AMCT toolkit usage