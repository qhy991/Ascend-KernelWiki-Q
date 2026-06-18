---
id: technique-pr-samples-2547
title: "PR Insight: Ascend/samples #2547"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2547"
---

# PR Insight: Ascend/samples #2547

**Title:** 修复Matmul常量化bug

## Overview
This PR fixes a bug in the matmul constant quantization samples (from PRs #2407, #2469). The bug likely affected correctness or performance of quantized constant weight handling.

## Technical Significance
Quantization bugs can cause subtle accuracy issues. Fixing these ensures quantized inference samples produce correct results and serve as reliable references for production deployments.

## Related
- `kernel-matmul-ascendc`, `technique-quantization`, `technique-format-conversion`