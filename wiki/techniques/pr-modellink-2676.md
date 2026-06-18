---
id: technique-pr-modellink-2676
title: "PR Insight: Ascend/ModelLink #2676"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspore
  - feature
  - communication
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2676"
---

# PR Insight: Ascend/ModelLink #2676

**Title:** add async_log_allreduce for mindspore

## Overview
This PR adds async_log_allreduce functionality for the MindSpore backend. This feature likely enables asynchronous allreduce communication operations with logging support, improving overlapping of computation and communication in distributed training.

## Technical Significance
Asynchronous allreduce operations are critical for hiding communication latency in distributed training. By overlapping computation with communication, this optimization improves training throughput on Ascend NPUs, especially for large-scale distributed training scenarios with MindSpore.

## Related
- technique-hccl-optimization
- technique-cube-vector-overlap