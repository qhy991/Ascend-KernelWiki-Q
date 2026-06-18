---
id: technique-pr-samples-1830
title: "PR Insight: Ascend/samples #1830"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-op
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1830"
---

# PR Insight: Ascend/samples #1830

**Title:** commit AddCustomSample and LeakyReLUCustomSample

## Overview
This PR commits two custom operator samples: a general AddCustomSample and a specific LeakyReLUCustomSample. Custom operators allow developers to implement custom kernels using AscendC.

## Technical Significance
Custom operator samples are essential for teaching developers how to extend Ascend's operator library with domain-specific kernels. The LeakyReLU example demonstrates activation function implementation, which is a common operation in neural networks. These samples show the complete workflow for registering and executing custom operators on Ascend NPUs.

## Related
- `wiki-technique-custom-operator`
- `wiki-technique-ascendc`
- `kernel-activation`