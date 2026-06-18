---
id: technique-pr-mindspeed-1180
title: "PR Insight: Ascend/MindSpeed #1180"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - hook
  - gradient
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1180"
---

# PR Insight: Ascend/MindSpeed #1180

**Title:** [master]bugfix:调用save_tensors_hook接口导致weight没有main_grad属性

## Overview
This PR fixes a bug where calling the `save_tensors_hook` interface caused weights to lose their `main_grad` attribute. This attribute is important for gradient accumulation and optimization in training workflows.

## Technical Significance
The `main_grad` attribute is critical for proper gradient handling during training on Ascend NPUs. This fix ensures that gradient accumulation and optimization work correctly when using tensor save hooks, preventing training errors or incorrect weight updates.

## Related
- technique-data-reuse