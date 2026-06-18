---
id: technique-pr-sgl-kernel-npu-129
title: "PR Insight: sgl-project/sgl-kernel-npu #129"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - cleanup
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/129"
---

# PR Insight: sgl-project/sgl-kernel-npu #129

**Title:** Delete left useless code [FusedDeepMoe Operator]

## Overview
This PR removes unused code left over from PR #123, cleaning up the grouped matmul kernel implementation for FusedDeepMoe.

## Technical Significance
Code cleanup reduces maintenance burden and prevents confusion from unused code paths. Removing dead code is especially important in performance-critical kernels where extraneous logic can obscure optimization opportunities.

## Related
- `technique-moe`, `kernel-matmul-ascendc`