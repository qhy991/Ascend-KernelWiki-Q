---
id: technique-pr-modellink-2380
title: "PR Insight: Ascend/ModelLink #2380"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - pipeline
  - testing
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2380"
---

# PR Insight: Ascend/ModelLink #2380

**Title:** fix:pipeline报错用例，删除看护用例中的save参数

## Overview
This PR fixes a pipeline execution error by removing the `save` parameter from pipeline test cases. The change addresses incorrect configuration that was causing test failures during pipeline parallel execution scenarios.

## Technical Significance
Pipeline parallelism is a key distributed training technique for large models on Ascend clusters. Incorrect parameter configuration can cause synchronization issues between pipeline stages, leading to training failures. Removing the improperly configured `save` parameter ensures clean pipeline execution, particularly for test workflows that validate cross-stage communication and gradient flow in multi-node training setups.

## Related
- `technique-pipeline-scheduling`
- `technique-hccl-optimization`