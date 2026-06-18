---
id: technique-pr-samples-981
title: "PR Insight: Ascend/samples #981"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - python
  - import
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/981"
---

# PR Insight: Ascend/samples #981

**Title:** add import module

## Overview
Adds a missing import module to the Python sample code, resolving import errors that would prevent the sample from running.

## Technical Significance
Missing imports are common beginner errors. This fix ensures the sample code is self-contained and can run without modification, improving user experience.

## Related
- `technique-python-binding` / `technique-api-design`
