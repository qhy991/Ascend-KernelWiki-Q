---
id: technique-pr-samples-2113
title: "PR Insight: Ascend/samples #2113"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - leakyrelu
  - async
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2113"
---

# PR Insight: Ascend/samples #2113

**Title:** add ascendc matmul leakyrelu async sample

## Overview
This PR adds an asynchronous execution sample for the MatMulLeakyReLU fused operator, demonstrating how to use streams and events to achieve overlapping computation and data transfer.

## Technical Significance
Shows async programming patterns on Ascend hardware, enabling higher throughput by overlapping kernel execution with memory operations. This is essential for maximizing utilization in multi-operator inference pipelines.

## Related
- `technique-operator-fusion`
- `technique-event-sync`
- `technique-pipeline-scheduling`