---
id: technique-pr-mindspeed-1450
title: "PR Insight: Ascend/MindSpeed #1450"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - performance
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1450"
---

# PR Insight: Ascend/MindSpeed #1450

**Title:** perf: all_to_all_single supports non-uniform scatter and gather sizes

## Overview
This PR extends all_to_all_single collective operation to support non-uniform scatter and gather sizes. This optimization allows more flexible and efficient data distribution patterns in distributed training.

## Technical Significance
Enables more efficient all-to-all communication patterns by supporting non-uniform data distribution, which is essential for MoE and other advanced parallelism strategies. This optimization reduces communication overhead and improves overall training efficiency.

## Related
- `technique-hccl-optimization`
- `kernel-moe`