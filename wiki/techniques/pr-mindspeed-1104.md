---
id: technique-pr-mindspeed-1104
title: "PR Insight: Ascend/MindSpeed #1104"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - vpp
  - communication
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1104"
---

# PR Insight: Ascend/MindSpeed #1104

**Title:** 【master】VPP send recv 优化

## Overview
This PR optimizes VPP (likely Virtual Pipeline Parallelism or similar) send and receive operations. These optimizations improve the efficiency of data transfer between pipeline stages in distributed training.

## Technical Significance
Efficient send/receive operations are critical for pipeline parallelism performance on Ascend clusters using HCCS interconnect. This optimization reduces communication overhead and improves pipeline throughput, enabling faster training of large models across multiple Ascend NPUs.

## Related
- technique-hccl-optimization
- technique-communication-optimization
- hw-hccs