---
id: technique-pr-samples-2746
title: "PR Insight: Ascend/samples #2746"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tiling
  - shape
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2746"
---

# PR Insight: Ascend/samples #2746

**Title:** 适配tiling shape

## Overview
This PR adapts tiling strategies to handle different tensor shapes. The change likely improves how samples handle various input dimensions, ensuring that tiling logic works correctly across different problem sizes.

## Technical Significance
Proper shape handling in tiling is critical for performance correctness. Incorrect tiling for certain shapes can lead to memory access violations, incorrect results, or suboptimal performance. This fix ensures samples work reliably across diverse workloads.

## Related
- technique-nz-tiling
- technique-bank-conflict-avoidance