---
id: technique-pr-modellink-2181
title: "PR Insight: Ascend/ModelLink #2181"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - evaluation
  - distributed
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2181"
---

# PR Insight: Ascend/ModelLink #2181

**Title:** ceval 模块增加模版 和 支持 DP 评估

## Overview
This PR adds templates to the CEval evaluation module and supports data parallel evaluation, enabling more flexible and scalable evaluation workflows for language models.

## Technical Significance
Data parallel evaluation support allows evaluation on larger datasets across multiple devices, while templates improve evaluation flexibility for different model architectures and prompt formats.

## Related
- `technique-evaluation` / `technique-data-parallel` / `technique-ceval`