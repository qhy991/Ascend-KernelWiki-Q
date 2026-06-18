---
id: technique-pr-modellink-2190
title: "PR Insight: Ascend/ModelLink #2190"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - optimizer
  - weight-conversion
  - nooplayer
  - dpp
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2190"
---

# PR Insight: Ascend/ModelLink #2190

**Title:** 新增优化器权重转换nooplayer/dpp功能

## Overview
Adds no-op layer and DPP (Data Parallel Pipeline) weight conversion functionality for optimizers. This enables proper weight handling for models that contain no-op layers or use DPP parallelism.

## Technical Significance
Expands weight conversion capabilities to support more complex model architectures and parallelism strategies. Proper handling of no-op layers and DPP is essential for maintaining correctness during optimizer state management and checkpoint conversion.

## Related
- technique-hccl-optimization
- technique-data-reuse