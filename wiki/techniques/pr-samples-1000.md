---
id: technique-pr-samples-1000
title: "PR Insight: Ascend/samples #1000"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dvpp
  - jpegd
  - cleanup
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1000"
---

# PR Insight: Ascend/samples #1000

**Title:** Delete JPEGD DDK count print

## Overview
Removes debug print statements showing DDK count from the JPEGD decoder sample code.

## Technical Significance
Cleanup of debug output improves production readiness by reducing log noise and potential performance overhead from excessive printing.

## Related
- `technique-dvpp-optimization`
