---
id: technique-pr-samples-1660
title: "PR Insight: Ascend/samples #1660"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - qat
  - quantization
  - quantization-aware-training
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1660"
---

# PR Insight: Ascend/samples #1660

**Title:** 添加QAT单算子量化感知训练sample

## Overview
This PR adds a QAT (Quantization-Aware Training) single-operator sample, demonstrating how to apply quantization-aware training techniques to individual operators for Ascend deployment.

## Technical Significance
QAT simulates quantization effects during training to produce models that maintain accuracy when deployed with quantized weights. Single-operator QAT is useful for understanding quantization behavior at a granular level and for developing custom operators with quantization support.

## Related
- technique-quantization
- technique-qat