---
id: technique-pr-mindspeed-2550
title: "PR Insight: Ascend/MindSpeed #2550"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - pp
  - forward-only
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2550"
---

# PR Insight: Ascend/MindSpeed #2550

**Title:** bugfix 多参数pp forward only修复

## Overview
This PR fixes a bug in multi-parameter pipeline parallel (PP) forward-only mode. The issue affected forward pass execution when using multiple parameter groups or configurations in pipeline parallel training.

## Technical Significance
Pipeline parallelism splits model layers across devices. Forward-only mode is useful for inference or validation. Fixing bugs in multi-parameter scenarios ensures correct execution when different parameter groups have different pipeline configurations.

## Related
- `technique-pipeline-scheduling`