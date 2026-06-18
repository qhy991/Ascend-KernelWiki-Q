---
id: technique-pr-samples-1226
title: "PR Insight: Ascend/samples #1226"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg
  - resize
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1226"
---

# PR Insight: Ascend/samples #1226

**Title:** Add resize tinyjpegd

## Overview
This PR adds resize functionality to the tinyjpegd (tiny JPEG decoder) sample application.

## Technical Significance
Combining JPEG decoding with resize operations is a common preprocessing step in CV pipelines. On Ascend hardware, fusing these operations can significantly improve performance by reducing memory movement. Resize operations benefit from vector unit acceleration and proper memory alignment in the unified buffer.

## Related
- technique-vector-unit
- technique-operator-fusion
- hw-unified-buffer