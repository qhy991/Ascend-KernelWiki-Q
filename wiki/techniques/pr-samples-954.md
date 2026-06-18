---
id: technique-pr-samples-954
title: "PR Insight: Ascend/samples #954"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - acllite
  - dvpp
  - feature-add
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/954"
---

# PR Insight: Ascend/samples #954

**Title:** add acllite dvpp api

## Overview
Adds DVPP APIs to the acllite library, providing C++ wrappers for hardware-accelerated preprocessing operations.

## Technical Significance
Integrating DVPP into acllite makes it easier for C++ developers to leverage hardware preprocessing without dealing with low-level ACL APIs. This is important for building efficient inference pipelines.

## Related
- `technique-dvpp-optimization` / `technique-api-design` / `technique-preprocessing`
