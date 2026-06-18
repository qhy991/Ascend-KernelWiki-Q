---
id: technique-pr-samples-2713
title: "PR Insight: Ascend/samples #2713"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - matmul
  - leakyrelu
  - documentation
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2713"
---

# PR Insight: Ascend/samples #2713

**Title:** matmul_leakyrelu_custom修复了注释 ASCEND310P 并删除了冗余句号

## Overview
This PR updates documentation in the matmul_leakyrelu_custom sample, fixing references to ASCEND310P and removing redundant punctuation from comments. This is a documentation-only change that improves code clarity.

## Technical Significance
Clear documentation is essential for samples that developers use as reference implementations. Fixing architecture-specific comments and removing redundant punctuation improves the maintainability and readability of the sample code.

## Related
- kernel-matmul-ascendc
- technique-operator-fusion