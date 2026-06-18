---
id: technique-pr-samples-716
title: "PR Insight: Ascend/samples #716"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - pytorch
  - quantization
  - auto-calibration
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/716"
---

# PR Insight: Ascend/samples #716

**Title:** fix amct pytorch auto calibration sample

## Overview
This PR fixes issues in the AMCT (Ascend Model Compression Toolkit) PyTorch auto-calibration sample, addressing bugs that prevent proper automatic calibration during quantization workflows.

## Technical Significance
Fixing AMCT PyTorch auto-calibration samples ensures that developers can successfully perform automated calibration for PyTorch models, which is critical for accurate quantization and optimal model performance on Ascend hardware.

## Related
- N/A (quantization bugfix)