---
id: technique-pr-samples-1344
title: "PR Insight: Ascend/samples #1344"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - vdec
  - jpegd
  - pngd
  - signal-handling
  - dvpp
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1344"
---

# PR Insight: Ascend/samples #1344

**Title:** 【轻量级 PR】：解决vdec、jpegd、pngd demo运行时ctrl+c无法退出问题

## Overview
This PR fixes an issue where the VDEC, JPEGD, and PNGD demo programs could not exit when Ctrl+C was pressed. The changes improve signal handling for graceful termination.

## Technical Significance
Proper signal handling is important for user experience and resource management. The fix ensures that DVPP demos can be cleanly interrupted without leaving resources in an inconsistent state.

## Related
- `technique-dvpp`
- `pattern-signal-handling`