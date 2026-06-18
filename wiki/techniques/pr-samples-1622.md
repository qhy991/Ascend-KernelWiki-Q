---
id: technique-pr-samples-1622
title: "PR Insight: Ascend/samples #1622"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - model-output
  - api
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1622"
---

# PR Insight: Ascend/samples #1622

**Title:** GetModelOutputInfo bug fix

## Overview
This PR fixes a bug in the GetModelOutputInfo API function, correcting issues with retrieving model output information.

## Technical Significance
GetModelOutputInfo is used to query the shape, data type, and format of model outputs, which is essential for post-processing. Bugs in this API can cause incorrect output interpretation or crashes, affecting the entire inference pipeline's reliability.

## Related
- technique-acl-api