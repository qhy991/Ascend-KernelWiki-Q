---
id: technique-pr-samples-2008
title: "PR Insight: Ascend/samples #2008"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kernel-launch
  - api-unification
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2008"
---

# PR Insight: Ascend/samples #2008

**Title:** 统一Kernel直调入参

## Overview
This PR continues the effort to unify kernel invocation parameters across samples, further standardizing the interface for buffer management, workspace allocation, and kernel configuration.

## Technical Significance
Strengthens consistency across all kernel samples, making it easier for developers to understand and reuse kernel launching patterns. The unified interface reduces code duplication and maintenance burden.

## Related
- `technique-instruction-queue`
- `kernel-matmul-ascendc`