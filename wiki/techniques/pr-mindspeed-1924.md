---
id: technique-pr-mindspeed-1924
title: "PR Insight: Ascend/MindSpeed #1924"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - communication
  - all-to-all
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1924"
---

# PR Insight: Ascend/MindSpeed #1924

**Title:** feat: all_to_all接口增加对scatter_size,gather_size两者都不能整除world_size的支持

## Overview
This PR enhances the all_to_all communication interface to support cases where neither scatter_size nor gather_size is divisible by world_size. This enables more flexible data redistribution patterns in distributed training.

## Technical Significance
All-to-all communication is fundamental to MoE and other distributed workloads. Supporting non-divisible sizes is important for handling uneven data distribution and enables more efficient communication patterns when perfect load balancing isn't possible.

## Related
- technique-hccl-optimization
- all-to-all communication
- distributed training