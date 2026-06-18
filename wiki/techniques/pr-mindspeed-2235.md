---
id: technique-pr-mindspeed-2235
title: "PR Insight: Ascend/MindSpeed #2235"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - pipeline-parallel
  - communication
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2235"
---

# PR Insight: Ascend/MindSpeed #2235

**Title:** 重构：pp特性的optimize_send_recv

## Overview
This PR refactors the optimize_send_recv feature in the pipeline parallel implementation. The optimization improves communication efficiency between pipeline stages by optimizing send and receive operations.

## Technical Significance
The optimize_send_recv feature is a critical performance optimization for pipeline parallel training on Ascend NPUs. By optimizing HCCL send and receive operations between pipeline stages, this feature reduces communication overhead and improves pipeline utilization. The refactoring improves code maintainability and may add new optimizations such as overlapping communication with computation, reducing synchronization points, or improving tensor transfer efficiency. This optimization is particularly important for models with many pipeline stages.

## Related
- `technique-hccl-optimization`
- `technique-pipeline-scheduling`