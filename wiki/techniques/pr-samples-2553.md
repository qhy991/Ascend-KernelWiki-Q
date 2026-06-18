---
id: technique-pr-samples-2553
title: "PR Insight: Ascend/samples #2553"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - workspace
  - code-quality
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2553"
---

# PR Insight: Ascend/samples #2553

**Title:** AscendC samples, remove hard code workspace size

## Overview
This PR removes hardcoded workspace sizes across all AscendC samples, not just matmul. This systematic change improves the overall code quality and portability of the samples repository.

## Technical Significance
A comprehensive fix for hardcoded workspace sizes demonstrates best practices that should be followed in all AscendC code. The change makes samples more robust across different hardware configurations.

## Related
- `pattern-api-usage`, `hw-unified-buffer`