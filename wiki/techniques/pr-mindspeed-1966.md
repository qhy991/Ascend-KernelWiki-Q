---
id: technique-pr-mindspeed-1966
title: "PR Insight: Ascend/MindSpeed #1966"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - checkpoint
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1966"
---

# PR Insight: Ascend/MindSpeed #1966

**Title:** fix ema checkpointing method

## Overview
This PR fixes an issue with Exponential Moving Average (EMA) checkpointing in MindSpeed. The fix addresses how EMA states are saved and loaded during training checkpoints.

## Technical Significance
EMA checkpointing is important for training stability and model weight smoothing. Fixing the checkpointing method ensures that EMA states are properly persisted and recovered, preventing model quality degradation during training resumption.

## Related
- checkpoint patterns
- training-optimization