---
id: technique-pr-samples-2442
title: "PR Insight: Ascend/samples #2442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - aclnn
  - api
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2442"
---

# PR Insight: Ascend/samples #2442

**Title:** aclnn invoke

## Overview
This PR adds samples for invoking aclnn APIs. aclnn (Ascend Computing Language Neural Network) provides high-level neural network operator interfaces that are easier to use than direct kernel launches. The samples demonstrate how to call these APIs in practice.

## Technical Significance
aclnn is the recommended path for most inference workloads as it handles tiling, format conversion, and kernel selection automatically. These samples bridge the gap between the API documentation and real-world usage.

## Related
- `technique-operator-fusion`, `pattern-api-usage`