---
id: technique-pr-mindspeed-2224
title: "PR Insight: Ascend/MindSpeed #2224"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - pipeline-parallel
  - refactor
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2224"
---

# PR Insight: Ascend/MindSpeed #2224

**Title:** 重构：pp支持多shape参数传递

## Overview
This PR refactors pipeline parallel (PP) implementation to support passing multiple shape parameters. The change enables more flexible model partitioning and tensor shape handling across pipeline stages.

## Technical Significance
Support for multiple shape parameters in pipeline parallel is crucial for handling variable-length sequences and dynamic batch sizes during training. This refactoring improves the flexibility of PP implementation on Ascend NPUs, allowing models to handle varying input shapes without performance penalties. The optimization likely improves memory allocation efficiency and tensor communication patterns between pipeline stages, reducing idle time and improving overall training throughput.

## Related
- `technique-pipeline-scheduling`
- `technique-hccl-optimization`