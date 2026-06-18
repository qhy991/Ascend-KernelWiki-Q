---
id: technique-pr-mindspeed-2328
title: "PR Insight: Ascend/MindSpeed #2328"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - test
  - recompute
  - ut
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2328"
---

# PR Insight: Ascend/MindSpeed #2328

**Title:** 【BUGFIX!!!】UT补充&amp;recompute修复

## Overview
This PR adds unit tests (UT补充) and fixes recompute functionality. The urgency of the bugfix (indicated by !!!) suggests a critical issue in the recompute implementation.

## Technical Significance
Adds comprehensive test coverage for recompute features and fixes critical bugs. Recompute is essential for memory optimization in large model training, and proper testing ensures reliability.

## Related
- `technique-recompute`
- `technique-memory-optimization`