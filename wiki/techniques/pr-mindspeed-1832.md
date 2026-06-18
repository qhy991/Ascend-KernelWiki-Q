---
id: technique-pr-mindspeed-1832
title: "PR Insight: Ascend/MindSpeed #1832"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - profiling
  - performance
  - monitoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1832"
---

# PR Insight: Ascend/MindSpeed #1832

**Title:** add profiler group name

## Overview
This PR adds group naming capability to the profiler in MindSpeed. The feature allows organizing profiling data into named groups for better analysis and visualization.

## Technical Significance
Profiler group names improve analysis of complex training workloads by enabling categorization of different execution phases, operator types, or parallelism strategies. This helps identify performance bottlenecks in specific components on Ascend NPUs.

## Related
- performance-optimization
- profiling techniques