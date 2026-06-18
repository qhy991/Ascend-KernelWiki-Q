---
id: technique-pr-samples-275
title: "PR Insight: Ascend/samples #275"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-op
  - cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/275"
---

# PR Insight: Ascend/samples #275

**Title:** delete dynamic Op: assign

## Overview
This PR removes the dynamic Assign operator sample, likely because the functionality is now provided by built-in operators or the sample is no longer maintained. It simplifies the codebase by removing obsolete examples.

## Technical Significance
Maintains codebase cleanliness by removing outdated operator samples, helping developers focus on current best practices and supported operator patterns in TBE/TIK development.

## Related
- `technique-operator-fusion`