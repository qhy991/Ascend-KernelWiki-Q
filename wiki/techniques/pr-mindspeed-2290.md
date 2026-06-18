---
id: technique-pr-mindspeed-2290
title: "PR Insight: Ascend/MindSpeed #2290"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - ripipe
  - bugfix
  - v2
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2290"
---

# PR Insight: Ascend/MindSpeed #2290

**Title:** fix: ripipe v2

## Overview
This PR fixes bugs in ripipe v2, the second version of the RIPipe pipeline optimization feature. The v2 version likely includes improvements over v1, and these fixes ensure the updated implementation works correctly.

## Technical Significance
Version 2 of pipeline optimizations often include significant improvements in efficiency or functionality. Bugfixes in v2 are critical for users to benefit from these improvements without encountering stability issues. This fix ensures RIPipe v2 can be reliably used in production training.

## Related
- `technique-pipeline-scheduling`
- `technique-activation-recompute`
- `pattern-version-stability`