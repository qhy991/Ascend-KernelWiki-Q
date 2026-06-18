---
id: technique-pr-samples-2154
title: "PR Insight: Ascend/samples #2154"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - configuration
  - rc
  - aicore-num
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2154"
---

# PR Insight: Ascend/samples #2154

**Title:** [DTS2024080627533]删除RC配置文件中的aicore_num参数

## Overview
This PR removes the aicore_num parameter from RC (Run Configuration) files, likely because this parameter is no longer needed or is auto-detected.

## Technical Significance
RC configuration files control runtime behavior. Removing auto-detectable parameters simplifies configuration and reduces potential for user error. This change reflects improvements in Ascend's hardware detection capabilities.

## Related
- `wiki-hardware-cube-unit`