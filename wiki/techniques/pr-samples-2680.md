---
id: technique-pr-samples-2680
title: "PR Insight: Ascend/samples #2680"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - ascendc
  - testing
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2680"
---

# PR Insight: Ascend/samples #2680

**Title:** 替换CCE_KT_TEST

## Overview
This PR replaces CCE_KT_TEST references in the codebase. The substitution updates test infrastructure or build configurations to use newer testing frameworks or APIs for AscendC kernel development.

## Technical Significance
Keeping test infrastructure up to date ensures compatibility with the latest CANN toolchain versions. Proper test frameworks are essential for validating kernel correctness and performance during development.

## Related
- `technique-operator-fusion`
- `hw-cube-unit`