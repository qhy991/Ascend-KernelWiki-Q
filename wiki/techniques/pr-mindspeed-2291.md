---
id: technique-pr-mindspeed-2291
title: "PR Insight: Ascend/MindSpeed #2291"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - overlap
  - param-gather
  - bugfix
  - precision
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2291"
---

# PR Insight: Ascend/MindSpeed #2291

**Title:** 【BUGFIX!】overlap_param_gather精度修正

## Overview
This PR fixes a precision issue in the overlap_param_gather functionality. Overlapping parameter gathering with computation is a technique to hide communication latency, but it requires careful handling to maintain numerical precision.

## Technical Significance
Precision bugs in parameter gathering can cause model training to diverge or produce incorrect results. The fix likely involves ensuring proper data types, alignment, or conversion during the overlapped gather operation. This is critical for distributed training where parameters are gathered across multiple devices.

## Related
- `technique-communication-overlap`
- `technique-param-gather`
- `pattern-precision-handling`