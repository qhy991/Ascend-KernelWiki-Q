---
id: technique-pr-mindspeed-2468
title: "PR Insight: Ascend/MindSpeed #2468"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - dualpipev
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2468"
---

# PR Insight: Ascend/MindSpeed #2468

**Title:** [bugfix]dualpipev兼容空层

## Overview
This PR fixes dualpipev (dual pipeline parallelism) compatibility with empty layers. Empty layers are no-op layers that may appear in model architectures for compatibility or placeholder purposes.

## Technical Significance
Ensures dual pipeline parallelism works correctly even when models contain empty layers. This prevents crashes or incorrect execution in pipeline parallel training scenarios with models that have placeholder layers.

## Related
- `technique-pipeline-scheduling`
- `technique-distributed-training`