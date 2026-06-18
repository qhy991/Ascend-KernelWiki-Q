---
id: technique-pr-mindspeed-1141
title: "PR Insight: Ascend/MindSpeed #1141"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - noop
  - layer
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1141"
---

# PR Insight: Ascend/MindSpeed #1141

**Title:** [master]bugfix:noop_layer设置为非首尾层

## Overview
This PR fixes a bug where noop_layer (no-operation layer) could be incorrectly set as the first or last layer. Noop layers are used for structural alignment and should not occupy model boundary positions.

## Technical Significance
Correct placement of noop layers is important for proper model structure and optimization on Ascend NPUs. This fix ensures noop layers are positioned correctly within the model architecture, preventing issues with pipeline parallelism or other optimizations that depend on layer ordering.

## Related
- technique-pipeline-scheduling