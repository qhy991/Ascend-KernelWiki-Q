---
id: technique-pr-samples-1401
title: "PR Insight: Ascend/samples #1401"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - context
  - device-management
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1401"
---

# PR Insight: Ascend/samples #1401

**Title:** fix set context failed on device

## Overview
This PR fixes a bug where setting the context on the device was failing. The fix addresses a runtime initialization or configuration issue that prevented proper device context setup.

## Technical Significance
Proper device context initialization is fundamental for Ascend runtime operations. This fix ensures samples can correctly establish and manage device contexts for inference and computation.

## Related
- technique-device-management
- technique-runtime-initialization