---
id: technique-pr-samples-462
title: "PR Insight: Ascend/samples #462"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aicpu
  - custom-operator
  - so-file
  - bugfix
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/462"
---

# PR Insight: Ascend/samples #462

**Title:** fix aicpu custom so to 440

## Overview
This PR fixes an issue with AICPU custom operator shared library (.so file) compilation or versioning, specifically related to version 440 compatibility or build configuration.

## Technical Significance
Resolves build or runtime issues with AICPU custom operators, ensuring that custom shared libraries compile and load correctly on the specified CANN version.

## Related
- `pattern-build-system`
- `technique-operator-development`