---
id: technique-pr-samples-1231
title: "PR Insight: Ascend/samples #1231"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - conv2d
  - matmul
  - l2-mode
  - cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1231"
---

# PR Insight: Ascend/samples #1231

**Title:** conv2d/matmul算子样例删除l2_mode

## Overview
This PR removes the l2_mode parameter and configuration from conv2d and matmul operator samples, simplifying the operator interface as this mode is no longer required or supported.

## Technical Significance
Simplifies operator development by removing deprecated configuration options, making the samples more aligned with current best practices and reducing confusion for new developers.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`