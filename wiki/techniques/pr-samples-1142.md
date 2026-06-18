---
id: technique-pr-samples-1142
title: "PR Insight: Ascend/samples #1142"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - operators
  - directory-rename
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1142"
---

# PR Insight: Ascend/samples #1142

**Title:** 算子目录cust_impl---->custom_impl

## Overview
This PR renames the operator directory from "cust_impl" to "custom_impl". This is a naming convention change to clarify that the directory contains custom operator implementations rather than customer implementations.

## Technical Significance
Directory naming affects code organization and developer understanding. The change from "cust_impl" to "custom_impl" provides more accurate terminology for custom operators, reducing confusion between customer-specific implementations and general custom operator development patterns on Ascend.

## Related
- Custom operator development
- Code organization conventions
- Operator implementation structure