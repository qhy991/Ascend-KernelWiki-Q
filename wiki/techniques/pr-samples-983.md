---
id: technique-pr-samples-983
title: "PR Insight: Ascend/samples #983"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dvpp
  - jpegd
  - pngd
  - ddk
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/983"
---

# PR Insight: Ascend/samples #983

**Title:** Add end-of-line symbol in JPEGD/PNGD DDK

## Overview
Adds missing end-of-line symbols in JPEGD and PNGD DDK code, likely fixing formatting or parsing issues in these DVPP operations.

## Technical Significance
Proper line termination is important for cross-platform compatibility and correct file parsing. This fix ensures JPEG/PNG decoding operations work correctly across different environments.

## Related
- `technique-dvpp-optimization`
