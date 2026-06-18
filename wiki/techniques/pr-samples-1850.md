---
id: technique-pr-samples-1850
title: "PR Insight: Ascend/samples #1850"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - uniquecust
  - inference
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1850"
---

# PR Insight: Ascend/samples #1850

**Title:** uniquecust add rt1 infershaperange

## Overview
This PR adds dynamic shape range support (rt1 infershaperange) to the uniquecust sample. This feature allows the inference engine to handle tensors with variable dimensions during model execution.

## Technical Significance
Dynamic shape support is essential for processing variable-length inputs in production scenarios, such as natural language processing or computer vision applications with different image sizes. The uniquecust sample's enhancement demonstrates how to configure shape inference for flexible input handling on Ascend NPUs.

## Related
- `wiki-technique-dynamic-shape`
- `wiki-technique-inference`