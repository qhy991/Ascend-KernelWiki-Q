---
id: technique-pr-catlass-137
title: "PR Insight: Ascend/catlass #137"
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
  - "https://gitee.com/ascend/catlass/pulls/137"
---

# PR Insight: Ascend/catlass #137

**Title:** remove matmul bias

## Overview
This PR is a follow-up to remove matmul bias functionality from catlass. It continues the refactoring to simplify the API or reorganize bias handling in the operator stack.

## Technical Significance
Consistent removal of bias functionality across all matmul variants ensures API uniformity. This reduces confusion and simplifies the integration surface for applications using catlass on Ascend hardware.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`