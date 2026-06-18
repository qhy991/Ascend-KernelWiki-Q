---
id: technique-pr-samples-1346
title: "PR Insight: Ascend/samples #1346"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - dvpp
  - vdec
  - bugfix
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1346"
---

# PR Insight: Ascend/samples #1346

**Title:** 【轻量级 PR】：删除不支持的多余命令参数OneStreamBuffer

## Overview
This PR removes the unsupported OneStreamBuffer command parameter from the samples. This parameter was not supported in the API and was causing confusion or errors.

## Technical Significance
Cleaning up unsupported parameters improves sample accuracy and prevents API misuse. This ensures developers don't try to use features that don't exist in the DVPP API.

## Related
- `technique-dvpp`
- `pattern-api-cleanup`