---
id: technique-pr-samples-1084
title: "PR Insight: Ascend/samples #1084"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - model-shape
  - inference
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1084"
---

# PR Insight: Ascend/samples #1084

**Title:** 增加选择模型shape

## Overview
This PR adds functionality to select model shapes in the samples. The enhancement allows users to configure or choose different model input/output shapes during inference operations.

## Technical Significance
Model shape selection is important for handling dynamic models, multiple input resolutions, or different batch sizes. This feature enables flexible inference configurations, allowing the same model to process inputs with varying dimensions or batch requirements on Ascend NPU.

## Related
- Model shape configuration
- Dynamic inference
- Input size selection
- ACL model API