---
id: technique-pr-samples-1144
title: "PR Insight: Ascend/samples #1144"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpegd
  - error-handling
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1144"
---

# PR Insight: Ascend/samples #1144

**Title:** add return in jpegd performance

## Overview
This PR adds a return statement in the JPEG decoder (JPEGD) performance measurement code. This likely ensures proper early return from error conditions or completes performance measurement execution flow correctly.

## Technical Significance
Proper return handling in performance measurement code prevents execution from continuing after errors or incomplete measurements. This fix ensures accurate performance data collection and prevents undefined behavior in benchmarking workflows for JPEG decoding on Ascend NPU.

## Related
- JPEG decoder (JPEGD) performance benchmarking
- Error handling patterns
- Performance measurement workflows