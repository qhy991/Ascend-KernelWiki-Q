---
id: technique-pr-samples-1288
title: "PR Insight: Ascend/samples #1288"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - samples
  - shell
  - execution
  - multi-model
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1288"
---

# PR Insight: Ascend/samples #1288

**Title:** 修改运行sample_run的方式，兼容多个模型

## Overview
This PR modifies how sample_run is executed to support multiple models. The changes improve the execution script to handle different model scenarios.

## Technical Significance
Supporting multiple models in sample execution improves flexibility and allows developers to test and benchmark different models using the same sample infrastructure.

## Related
- `pattern-execution-script`
- `pattern-multi-model`