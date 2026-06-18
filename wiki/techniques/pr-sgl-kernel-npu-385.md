---
id: technique-pr-sgl-kernel-npu-385
title: "PR Insight: sgl-project/sgl-kernel-npu #385"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - batch-size
  - bugfix
  - moe
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/385"
---

# PR Insight: sgl-project/sgl-kernel-npu #385

**Title:** [WIP] Fix bs zero for deepep

## Overview
This PR fixes issues with zero batch size handling in DeepEP operators across A2 and A3 architectures. The modifications remove batch size padding when partial ranks have bs=0, supporting dispatch, combine, and fused_deep_moe operations for scenarios where some ranks receive no tokens.

## Technical Significance
Properly handling zero batch size across ranks is essential for elastic training and inference where token distribution may be uneven. The fix ensures DeepEP operators work correctly in heterogeneous batch scenarios where some ranks might not receive any tokens due to load balancing or routing decisions.

## Related
- `kernel-deepep-dispatch`, `kernel-deepep-combine`, `kernel-fused-deep-moe`, `technique-bugfix`