---
id: technique-pr-catlass-128
title: "PR Insight: Ascend/catlass #128"
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
  - "https://gitee.com/ascend/catlass/pulls/128"
---

# PR Insight: Ascend/catlass #128

**Title:** OptimizedMatmul不padding时不启动aiv & 小m情况搬运优化 同步catlass-v1分支

## Overview
This PR synchronizes the OptimizedMatmul optimizations (disabling AIV when no padding needed, small-M data movement improvements) to the catlass-v1 branch.

## Technical Significance
Branch synchronization ensures that stable and development branches benefit from proven optimizations. Maintaining parity across branches reduces technical debt and ensures consistent performance characteristics for users on different catlass versions.

## Related
- `kernel-matmul-ascendc`
- `technique-double-buffering`