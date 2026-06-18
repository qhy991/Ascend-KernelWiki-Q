---
id: technique-pr-catlass-136
title: "PR Insight: Ascend/catlass #136"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - bias
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/136"
---

# PR Insight: Ascend/catlass #136

**Title:** remove matmul bias

## Overview
This PR removes matmul bias functionality from catlass. It may be a refactoring decision to simplify the API or move bias handling to a different layer in the operator stack.

## Technical Significance
Removing bias support changes the operator semantics and may affect how applications integrate with catlass. This decision could reflect a preference for explicit bias addition or outsourcing bias fusion to higher-level frameworks.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`