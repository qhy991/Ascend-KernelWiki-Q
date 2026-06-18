---
id: technique-pr-modellink-2302
title: "PR Insight: Ascend/ModelLink #2302"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - testing
  - pipeline
  - distributed
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2302"
---

# PR Insight: Ascend/ModelLink #2302

**Title:** 部分ut用例移动到pipeline

## Overview
Moves certain unit test cases to the pipeline testing infrastructure. This reorganization improves test execution efficiency and better aligns test cases with the appropriate pipeline stages for the ModelLink framework.

## Technical Significance
Improves the testing infrastructure for distributed training scenarios by optimizing where unit tests run in the CI/CD pipeline. This change helps ensure better test coverage for modellink's pipeline execution and distributed training workflows.

## Related
- technique-hccl-optimization
- technique-pipeline-scheduling