---
id: technique-pr-samples-619
title: "PR Insight: Ascend/samples #619"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - custom-operator
  - opp
  - packaging
  - deployment
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/619"
---

# PR Insight: Ascend/samples #619

**Title:** 增加custom opp 自定义算子包的删除功能

## Overview
This PR adds functionality for deleting custom operator (opp) packages in the custom operator samples. This allows users to remove previously installed custom operator packages from the Ascend runtime environment.

## Technical Significance
Being able to delete custom operator packages is essential for development and testing workflows where operators are frequently updated or removed. This functionality prevents conflicts between different versions of custom operators and supports clean development environments.

## Related
- Custom operators
- Operator packaging
- Deployment management
- Development workflows