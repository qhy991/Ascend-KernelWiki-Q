---
id: technique-pr-mindspeed-1038
title: "PR Insight: Ascend/MindSpeed #1038"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - eod
  - recomputation
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1038"
---

# PR Insight: Ascend/MindSpeed #1038

**Title:** 【BugFix】EoD适配重计算逻辑

## Overview
This PR fixes recomputation logic adaptation for EoD (likely Expert-on-Demand or similar feature). Recomputation trades compute for memory by recalculating values instead of storing them.

## Technical Significance
Proper recomputation adaptation is critical for memory-efficient training on Ascend NPUs. This fix ensures EoD features work correctly with MindSpeed's recomputation pipeline, enabling efficient memory usage while maintaining correct gradient computation.

## Related
- technique-data-reuse
- technique-memory-optimization