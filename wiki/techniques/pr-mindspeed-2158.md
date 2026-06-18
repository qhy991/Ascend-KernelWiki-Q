---
id: technique-pr-mindspeed-2158
title: "PR Insight: Ascend/MindSpeed #2158"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - profiling
  - performance
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2158"
---

# PR Insight: Ascend/MindSpeed #2158

**Title:** refactor: tflops计算和profiling采集重构

## Overview
This PR refactors TFLOPS calculation and profiling data collection in MindSpeed. The change improves the accuracy and efficiency of performance metrics measurement during training.

## Technical Significance
Accurate TFLOPS calculation and profiling are essential for measuring training performance and identifying bottlenecks on Ascend NPUs. The refactoring improves the collection of kernel execution times, memory bandwidth utilization, and communication overhead metrics. Better profiling data enables more informed optimization decisions and helps identify performance issues such as memory-bound kernels, communication stalls, or inefficient tensor parallel patterns. This optimization is particularly important for achieving peak hardware utilization and comparing performance across different model configurations.

## Related
- `technique-event-sync`
- `technique-instruction-queue`