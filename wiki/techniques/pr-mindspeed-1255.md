---
id: technique-pr-mindspeed-1255
title: "PR Insight: Ascend/MindSpeed #1255"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - flops
  - memory
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1255"
---

# PR Insight: Ascend/MindSpeed #1255

**Title:** Flops计算中移除调用at::empty，避免shape过大构造导致内存不足卡死问题

## Overview
This PR removes `at::empty` calls from FLOPS (floating point operations) calculation to prevent out-of-memory issues when constructing large tensors. The fix addresses a problem where large shapes would cause memory exhaustion during performance metric calculations.

## Technical Significance
Performance monitoring should not interfere with training execution. This fix ensures FLOPS calculation doesn't consume excessive memory on Ascend NPUs, preventing crashes during profiling of large models or batch sizes.

## Related
- technique-memory-optimization