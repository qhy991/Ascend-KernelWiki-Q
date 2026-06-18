---
id: technique-pr-samples-75
title: "PR Insight: Ascend/samples #75"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-op
  - interface
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/75"
---

# PR Insight: Ascend/samples #75

**Title:** Update interface for custom op

## Overview
This PR updates the interface definition for custom operator development, ensuring compatibility with the latest CANN API specifications. It standardizes the operator registration and invocation patterns.

## Technical Significance
Improves maintainability of custom operator samples by aligning with current TBE/TIK interface standards, reducing the learning curve for developers migrating custom operators to Ascend hardware.

## Related
- `technique-operator-fusion`