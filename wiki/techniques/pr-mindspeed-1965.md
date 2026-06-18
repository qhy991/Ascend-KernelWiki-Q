---
id: technique-pr-mindspeed-1965
title: "PR Insight: Ascend/MindSpeed #1965"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - communication
  - moe
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1965"
---

# PR Insight: Ascend/MindSpeed #1965

**Title:** 【特性】增加非均匀SP场景下的非均匀gather操作

## Overview
This PR adds support for non-uniform gather operations in non-uniform sequence parallelism (SP) scenarios. The feature enables handling of uneven data distribution across devices in sequence parallel training.

## Technical Significance
Non-uniform gather operations are essential for MoE and sequence parallel workloads where data distribution is not evenly balanced. This addition enables better support for dynamic batch sizes and uneven sequence lengths in distributed training on Ascend hardware.

## Related
- technique-hccl-optimization
- sequence-parallel patterns
- moe-routing techniques