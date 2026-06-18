---
id: technique-pr-mindspeed-2223
title: "PR Insight: Ascend/MindSpeed #2223"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - profiling
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2223"
---

# PR Insight: Ascend/MindSpeed #2223

**Title:** bug fix:auto_settings 导致profile失效

## Overview
This PR fixes a bug where auto_settings caused profiling to fail. The issue affected the ability to collect performance metrics and optimize training performance on Ascend NPUs.

## Technical Significance
Profiling is essential for understanding training bottlenecks and optimizing performance on Ascend hardware. This bug fix ensures that auto_settings configuration does not interfere with profiling tools, enabling accurate collection of kernel execution times, memory usage, and communication overhead. The fix likely addresses a configuration conflict or initialization order issue that prevented profiling hooks from being properly installed. Restoring profiling capability is crucial for performance tuning and debugging distributed training issues.

## Related
- `technique-event-sync`
- `technique-instruction-queue`