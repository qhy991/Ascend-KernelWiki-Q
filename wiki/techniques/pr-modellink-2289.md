---
id: technique-pr-modellink-2289
title: "PR Insight: Ascend/ModelLink #2289"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - pipeline
  - testing
  - ci
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2289"
---

# PR Insight: Ascend/ModelLink #2289

**Title:** fix:pipeline报错并调整ci ut/st运行顺序

## Overview
Fixes pipeline errors and adjusts the execution order of CI unit tests and system tests. This optimization improves the reliability and efficiency of the testing infrastructure.

## Technical Significance
Improves CI/CD pipeline stability and test execution efficiency. Proper test ordering helps identify issues earlier and reduces feedback time for developers working on complex distributed training features.

## Related
- technique-pipeline-scheduling