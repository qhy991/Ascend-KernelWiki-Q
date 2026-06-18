---
id: technique-pr-samples-1313
title: "PR Insight: Ascend/samples #1313"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - dynamic-batch
  - multi-device
  - multi-stream
  - inference
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1313"
---

# PR Insight: Ascend/samples #1313

**Title:** 添加动态batch功能以及多device多路支持

## Overview
This PR adds dynamic batch functionality and multi-device, multi-stream support to a sample. The changes enable more efficient inference workloads that can handle variable batch sizes across multiple Ascend devices.

## Technical Significance
Dynamic batching with multi-device support maximizes throughput for inference applications. The sample demonstrates advanced techniques for scaling inference workloads across multiple NPUs.

## Related
- `technique-dynamic-batching`
- `technique-hccl-optimization`
- `pattern-multi-device`