---
id: technique-pr-mindspeed-1018
title: "PR Insight: Ascend/MindSpeed #1018"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - mfu
  - fusion
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1018"
---

# PR Insight: Ascend/MindSpeed #1018

**Title:** mfu新增融合算子支持及ut bug fix

## Overview
This PR adds new fused operator support for MFU (likely Model FLOPS Utilization or similar metric) and fixes bugs in unit tests. Fused operators combine multiple operations for improved performance.

## Technical Significance
Fused operators improve performance on Ascend NPUs by reducing memory access and kernel launch overhead. Adding MFU support for these operators enables accurate performance measurement of optimized code, while unit test fixes ensure reliable validation.

## Related
- technique-operator-fusion