---
id: technique-pr-samples-2755
title: "PR Insight: Ascend/samples #2755"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - ascendc
  - static-tensor
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2755"
---

# PR Insight: Ascend/samples #2755

**Title:** add static tensor program samples

## Overview
This PR adds samples demonstrating static tensor programming in AscendC. Static tensor programming uses compile-time known tensor shapes for optimization.

## Technical Significance
Static tensor programming enables compile-time optimizations like loop unrolling, memory layout optimization, and instruction selection. These samples help developers understand when and how to use static tensor programming for better performance.

## Related
- `pattern-static-tensor-optimization`, `pattern-compile-time-optimization`