---
id: technique-pr-modellink-2344
title: "PR Insight: Ascend/ModelLink #2344"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - testing
  - pipeline
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2344"
---

# PR Insight: Ascend/ModelLink #2344

**Title:** 修复流水失败后继续执行后续用例的BUG

## Overview
This PR fixes a bug where test execution continues to subsequent test cases even after a pipeline failure. The fix ensures proper test failure handling and prevents cascading errors.

## Technical Significance
Proper test failure isolation is critical for debugging distributed training issues on Ascend hardware. When pipeline tests fail, continuing execution can mask root causes or cause resource contention. This fix ensures that pipeline failures halt execution appropriately, allowing engineers to diagnose issues without interference from subsequent test cases, improving debugging efficiency for complex multi-node training scenarios.

## Related
- `technique-testing-framework`
- `technique-pipeline-scheduling`