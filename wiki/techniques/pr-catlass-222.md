---
id: technique-pr-catlass-222
title: "PR Insight: Ascend/catlass #222"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - quantization
  - grouped-matmul
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/222"
---

# PR Insight: Ascend/catlass #222

**Title:** master分支同步dev分支quantGMM除cv ratio外的优化点

## Overview
This PR synchronizes quantized grouped matrix multiplication (quantGMM) optimizations from the dev branch to master, excluding the CV ratio optimization. It brings proven optimizations to the main branch.

## Technical Significance
Quantized grouped matmul is essential for efficient MoE inference and large-scale model serving. Synchronizing optimizations ensures that stable releases benefit from performance improvements while excluding features that may need further validation.

## Related
- `kernel-matmul-ascendc`
- `kernel-moe-ascendc`
- `technique-quantization`