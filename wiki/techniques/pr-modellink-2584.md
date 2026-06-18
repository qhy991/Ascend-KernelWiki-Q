---
id: technique-pr-modellink-2584
title: "PR Insight: Ascend/ModelLink #2584"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pipeline
  - bugfix
  - testing
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2584"
---

# PR Insight: Ascend/ModelLink #2584

**Title:** fix:pipeline及test文件路径

## Overview
This PR fixes file path issues in the pipeline implementation and test files. The changes correct incorrect path references that were causing failures or errors in pipeline workflows and test execution.

## Technical Significance
File path errors can cause training failures, test crashes, or incorrect file access. Correcting these paths ensures proper workflow execution, test coverage, and reproducibility when running pipeline training or tests on Ascend hardware.

## Related
- `technique-pipeline-scheduling`