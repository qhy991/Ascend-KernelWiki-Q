---
id: technique-pr-mindspeed-2042
title: "PR Insight: Ascend/MindSpeed #2042"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - parallel
  - auto-tuning
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2042"
---

# PR Insight: Ascend/MindSpeed #2042

**Title:** 融合auto_tuning 和auto_parallel方案

## Overview
This PR merges the auto_tuning and auto_parallel solutions in MindSpeed. The change integrates automatic performance tuning with automatic parallel strategy selection into a unified framework.

## Technical Significance
Merging auto_tuning and auto_parallel creates a more cohesive optimization framework for distributed training on Ascend NPUs. Auto_tuning optimizes kernel parameters, tiling strategies, and data layouts, while auto_parallel selects optimal parallel strategies (tensor parallel, pipeline parallel, data parallel). The integration enables coordinated optimization across both dimensions, potentially finding better combinations of parallel strategies and kernel optimizations. This unified approach simplifies configuration and can achieve better overall performance by considering trade-offs holistically.

## Related
- `technique-nz-tiling`
- `technique-hccl-optimization`