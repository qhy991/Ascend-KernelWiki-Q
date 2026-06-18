---
id: technique-pr-samples-1281
title: "PR Insight: Ascend/samples #1281"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - custom-operator
  - test
  - cleanup
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1281"
---

# PR Insight: Ascend/samples #1281

**Title:** samples仓中自定义算子相关test目录下的ut/st/bbit删除

## Overview
This PR removes UT (unit test), ST (system test), and BBIT directories from the custom operator test directories in the samples repository. The cleanup removes these test artifacts.

## Technical Significance
Removing test directories from samples keeps the repository focused on sample code rather than comprehensive test suites. This reduces repository size and simplifies the samples for end users.

## Related
- `technique-custom-operator`
- `pattern-repository-cleanup`