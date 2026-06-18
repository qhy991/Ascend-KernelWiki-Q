---
id: technique-pr-samples-2003
title: "PR Insight: Ascend/samples #2003"
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
  - "https://gitee.com/ascend/samples/pulls/2003"
---

# PR Insight: Ascend/samples #2003

**Title:** 统一Kernel直调入参

## Overview
This PR unifies the parameter passing interface for direct kernel invocation across different samples, standardizing how buffers, tiling parameters, and kernel configurations are passed to AscendC kernels.

## Technical Significance
Improves code consistency and reduces learning curve by establishing a uniform kernel launching pattern across all samples. This makes it easier to develop new custom kernels using established conventions.

## Related
- `technique-instruction-queue`
- `kernel-matmul-ascendc`