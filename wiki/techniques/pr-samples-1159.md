---
id: technique-pr-samples-1159
title: "PR Insight: Ascend/samples #1159"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - vdec
  - aclrt
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1159"
---

# PR Insight: Ascend/samples #1159

**Title:** fix bugs for vdec, no need call aclrtSubscribeReport when do vdec.

## Overview
This PR fixes bugs in the VDEC (video decoder) sample by removing unnecessary calls to aclrtSubscribeReport. The code previously called this API during VDEC operations, but it was determined to be unnecessary and potentially causing issues.

## Technical Significance
Removing unnecessary aclrtSubscribeReport calls simplifies the VDEC workflow and reduces overhead. This fix likely resolves performance issues or API conflicts that occurred when using the subscription API in conjunction with VDEC operations, leading to cleaner and more efficient video decode pipelines on Ascend NPU.

## Related
- Video decoder (VDEC) implementation
- ACL runtime API usage patterns
- Report subscription mechanisms
- Pipeline optimization for video processing