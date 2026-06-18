---
id: technique-pr-catlass-127
title: "PR Insight: Ascend/catlass #127"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - aiv
  - data-movement
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/127"
---

# PR Insight: Ascend/catlass #127

**Title:** !124 OptimizedMatmul不padding时不启动aiv &amp;小m情况搬运优化

## Overview
This PR is a follow-up or fix related to PR #124, addressing OptimizedMatmul optimizations for disabling AIV when padding is not needed and improving small-M data movement.

## Technical Significance
Iterative refinement of matmul optimizations is common as workloads evolve. Ensuring correct behavior when conditionally disabling AIV and optimizing small-M cases requires careful handling of edge cases and shape-specific tuning.

## Related
- `kernel-matmul-ascendc`
- `technique-double-buffering`