---
id: technique-pr-modellink-2182
title: "PR Insight: Ascend/ModelLink #2182"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2182"
---

# PR Insight: Ascend/ModelLink #2182

**Title:** boolq新增模版 & boolq支持DP评估

## Overview
This PR adds templates to the BoolQ evaluation module and supports data parallel evaluation, improving flexibility and scalability for boolean question answering benchmarks.

## Technical Significance
Data parallel support for BoolQ enables evaluation on larger datasets across multiple devices, while templates improve evaluation flexibility for different model architectures and prompt formats.

## Related
- `technique-evaluation` / `technique-data-parallel` / `technique-boolq`