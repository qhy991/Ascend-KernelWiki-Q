---
id: technique-pr-samples-1883
title: "PR Insight: Ascend/samples #1883"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - leakyrelu
  - elementwise
  - ascendc
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1883"
---

# PR Insight: Ascend/samples #1883

**Title:** 新增案例LeakyReluCustomSample

## Overview
This PR adds a LeakyReLU custom operator sample implemented in AscendC. The sample demonstrates how to implement the LeakyReLU activation function as a custom AscendC kernel, showing the kernel structure, element-wise computation patterns, and integration with inference frameworks.

## Technical Significance
LeakyReLU is a common activation function in neural networks that prevents dying ReLU problems by allowing small gradients for negative inputs. This sample demonstrates how to implement element-wise activation functions efficiently in AscendC, leveraging vector operations and proper memory access patterns for Ascend910/910B's compute units.

## Related
- `kernel-elementwise`
- `technique-activation-optimization`
- `pattern-custom-operator`