---
id: technique-pr-samples-470
title: "PR Insight: Ascend/samples #470"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - common-interface
  - refactoring
  - samples
  - api-design
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/470"
---

# PR Insight: Ascend/samples #470

**Title:** use commom interfence

## Overview
This PR refactors sample code to use common interfaces instead of platform-specific or duplicated implementations, improving code reuse and consistency across the repository.

## Technical Significance
Standardizes the codebase by consolidating interfaces, reducing code duplication and improving maintainability. Using common interfaces makes it easier to update and extend samples across different use cases.

## Related
- `pattern-refactoring`
- `pattern-api-design`