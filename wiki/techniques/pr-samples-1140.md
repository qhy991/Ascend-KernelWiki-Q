---
id: technique-pr-samples-1140
title: "PR Insight: Ascend/samples #1140"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - tik
  - tbe
  - kernel-development
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1140"
---

# PR Insight: Ascend/samples #1140

**Title:** add tik to add dsl

## Overview
This PR adds TIK (Tensor Iterator Kernel) support to include DSL (Domain Specific Language) functionality. The modification integrates TIK kernel development with DSL constructs, likely enabling more efficient kernel implementation patterns.

## Technical Significance
Integrating TIK with DSL provides developers with flexible kernel programming options on Ascend NPU. TIK offers fine-grained control over kernel execution, while DSL provides high-level abstractions. Combining both enables efficient kernel development with the right level of abstraction for different optimization scenarios.

## Related
- TIK kernel programming
- TBE DSL constructs
- Kernel development patterns
- AscendC programming models