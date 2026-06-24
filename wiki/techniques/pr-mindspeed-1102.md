---
id: technique-pr-mindspeed-1102
title: "PR Insight: Ascend/MindSpeed #1102"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - communication
  - tp
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1102"
---

# PR Insight: Ascend/MindSpeed #1102

**Title:** 高维张量并行通信隐藏参数可配置化（master）

## Overview
This PR makes high-dimensional tensor parallelism communication hiding parameters configurable. Communication hiding overlaps computation with communication to improve performance in distributed training scenarios.

## Technical Significance
Configurable communication hiding parameters allow users to tune performance for different network conditions and model configurations on Ascend clusters. This flexibility is important for optimizing distributed training throughput, especially when using HCCS (Ascend's high-speed interconnect) for tensor parallelism communication.

## Related
- technique-hccl-optimization
- technique-cube-vector-overlap
- wiki-hardware-hccs