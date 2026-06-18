---
id: technique-pr-samples-2661
title: "PR Insight: Ascend/samples #2661"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - custom-operator
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2661"
---

# PR Insight: Ascend/samples #2661

**Title:** [feature]fix add_custom

## Overview
This PR fixes the add_custom functionality in custom operator samples. The correction addresses issues with custom operator registration or execution, ensuring custom operators work correctly with Ascend runtime.

## Technical Significance
Custom operators are essential for extending Ascend capabilities beyond standard operators. Proper custom operator registration and execution workflows enable developers to implement domain-specific optimizations and integrate with the Ascend ecosystem.

## Related
- `technique-operator-fusion`
- `kernel-elementwise-ascendc`