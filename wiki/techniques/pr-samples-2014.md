---
id: technique-pr-samples-2014
title: "PR Insight: Ascend/samples #2014"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - elementwise
  - tbe-dsl
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2014"
---

# PR Insight: Ascend/samples #2014

**Title:** 将AddDsl算子的相关函数名由Add修改为AddDsl

## Overview
This PR renames functions in the AddDsl operator sample from "Add" to "AddDsl" to improve naming clarity and avoid conflicts. The refactoring updates function names to be more specific about the DSL-based Add operator implementation.

## Technical Significance
Clear naming conventions are important for sample code maintainability and for helping developers understand the difference between different operator implementations (e.g., DSL-based vs. TIK-based). This refactoring reduces confusion when learning AscendC operator development patterns.

## Related
- `technique-ascendc`
- `technique-tbe-dsl`