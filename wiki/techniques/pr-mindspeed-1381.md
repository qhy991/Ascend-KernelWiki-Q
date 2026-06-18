---
id: technique-pr-mindspeed-1381
title: "PR Insight: Ascend/MindSpeed #1381"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - recompute
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1381"
---

# PR Insight: Ascend/MindSpeed #1381

**Title:** 修复mcore分支recompute-in-bubble与激活函数重计算的兼容性问题

## Overview
This PR fixes compatibility issues between recompute-in-bubble and activation function recomputation on the mcore branch. The problem likely involved conflicts between different recomputation strategies or incorrect activation state management.

## Technical Significance
Resolves conflicts between bubble recomputation and activation recomputation, enabling both optimizations to work together correctly. This compatibility is essential for maximizing memory savings while maintaining correct gradient computation.

## Related
- `technique-recomputation`
- `pattern-bubble-computation`