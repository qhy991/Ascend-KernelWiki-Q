---
id: technique-pr-catlass-243
title: "PR Insight: Ascend/catlass #243"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - bugfix
  - memory-allocation
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/243"
---

# PR Insight: Ascend/catlass #243

**Title:** fix kernels running too slow due to allocating incorrectly calculated GM size

## Overview
This PR fixes a performance issue where kernels ran slowly due to incorrectly calculated global memory (GM) allocation size. The fix ensures proper memory sizing for kernel workspaces.

## Technical Significance
Incorrect GM allocation can cause memory fragmentation, excessive allocation overhead, or trigger suboptimal memory access patterns. This fix is critical for achieving expected performance in memory-bound matmul and attention kernels.

## Related
- `kernel-matmul-ascendc`
- `hw-global-memory`
- `technique-double-buffering`