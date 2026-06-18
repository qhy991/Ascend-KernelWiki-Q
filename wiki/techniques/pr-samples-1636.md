---
id: technique-pr-samples-1636
title: "PR Insight: Ascend/samples #1636"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - operator-info
  - workspace-size
  - validation
  - api
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1636"
---

# PR Insight: Ascend/samples #1636

**Title:** workspaceSize为可选字段，删除生成算子信息库时的字段校验

## Overview
This PR makes workspaceSize an optional field and removes the validation check for this field when generating the operator information library.

## Technical Significance
Workspace size validation was causing failures for operators that don't require explicit workspace specification. Making it optional increases flexibility in operator registration and allows the framework to handle workspace allocation automatically for operators where it's not user-defined.

## Related
- technique-operator-registration