---
id: technique-pr-samples-1010
title: "PR Insight: Ascend/samples #1010"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - pytorch
  - resnet
  - compression
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1010"
---

# PR Insight: Ascend/samples #1010

**Title:** add amct_pytorch resnet-101 compress feature sample

## Overview
Adds a new AMCT PyTorch sample demonstrating compression features for ResNet-101, showing how to apply model compression techniques to a deep residual network on Ascend hardware.

## Technical Significance
Expands the AMCT PyTorch sample coverage to deeper networks (ResNet-101 vs ResNet-50), demonstrating compression techniques at scale. Provides reference implementation for users working with larger models.

## Related
- `technique-quantization` / `technique-pruning` / `kernel-resnet`
