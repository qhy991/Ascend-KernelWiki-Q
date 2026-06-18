---
id: technique-pr-modellink-2274
title: "PR Insight: Ascend/ModelLink #2274"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - weight-conversion
  - deepseek3
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2274"
---

# PR Insight: Ascend/ModelLink #2274

**Title:** deepseek3权重转换默认值修正

## Overview
Fixes default values for DeepSeek3 weight conversion. The correction ensures proper default parameter settings during weight transformation processes.

## Technical Significance
Bugfix that ensures correct weight conversion behavior by using appropriate default values. Proper defaults are important for user experience and for preventing errors when users don't explicitly specify conversion parameters.

## Related
- technique-moe
- technique-data-reuse