---
id: technique-pr-samples-1997
title: "PR Insight: Ascend/samples #1997"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - bugfix
  - inference
  - port
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1997"
---

# PR Insight: Ascend/samples #1997

**Title:** fix sample infer_port

## Overview
This PR fixes an issue with the inference port configuration in a sample application. The fix corrects network port settings used for inference service endpoints.

## Technical Significance
Proper port configuration is essential for inference services to accept connections. This fix ensures sample applications correctly expose inference endpoints, allowing developers to test and validate model deployment on Ascend hardware.

## Related
- `technique-ascendc`