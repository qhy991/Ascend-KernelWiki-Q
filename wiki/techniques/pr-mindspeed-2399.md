---
id: technique-pr-mindspeed-2399
title: "PR Insight: Ascend/MindSpeed #2399"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - profile
  - optimization
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2399"
---

# PR Insight: Ascend/MindSpeed #2399

**Title:** 修改profile optimization_level=2

## Overview
This PR modifies profile optimization_level=2, likely adjusting the profiling and optimization settings in MindSpeed. Profile optimization levels control the degree of automatic optimization applied during training.

## Technical Significance
Adjusts optimization settings to improve performance or resolve issues with optimization level 2. Profile-based optimization helps identify and apply performance-critical transformations for Ascend NPU kernels.

## Related
- `technique-performance-profiling`
- `technique-optimization`