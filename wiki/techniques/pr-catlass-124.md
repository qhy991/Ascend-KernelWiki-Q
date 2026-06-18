---
id: technique-pr-catlass-124
title: "PR Insight: Ascend/catlass #124"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - aiv
  - data-movement
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/124"
---

# PR Insight: Ascend/catlass #124

**Title:** OptimizedMatmul不padding时不启动aiv & 小m情况搬运优化

## Overview
This PR optimizes OptimizedMatmul by disabling AIV (AI Vector) unit when padding is not needed and improving data movement for small M dimensions. The optimizations target both compute efficiency and memory bandwidth utilization.

## Technical Significance
Avoiding unnecessary AIV activation when padding isn't required saves power and reduces overhead. Small-M optimizations are critical because matmul with small batch or sequence dimensions can be memory-bound, making efficient data movement to the unified buffer essential for good performance.

## Related
- `kernel-matmul-ascendc`
- `technique-double-buffering`
- `technique-data-reuse`