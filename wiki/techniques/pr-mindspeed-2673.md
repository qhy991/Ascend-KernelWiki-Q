---
id: technique-pr-mindspeed-2673
title: "PR Insight: Ascend/MindSpeed #2673"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - feature
  - padding
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2673"
---

# PR Insight: Ascend/MindSpeed #2673

**Title:** 【feat.】支持动态padding功能

## Overview
This PR adds dynamic padding functionality to MindSpeed. The feature enables runtime adjustment of tensor padding to optimize memory layout and improve performance for variable-length inputs or tensor shapes.

## Technical Significance
Dynamic padding allows the framework to adapt tensor shapes to optimal memory layouts (e.g., NZ format alignment) at runtime, reducing memory waste and improving cache locality. This is particularly useful for NLP workloads with variable sequence lengths and can improve performance on Ascend hardware where memory alignment matters.

## Related
- `technique-nz-tiling`
- `technique-format-conversion`