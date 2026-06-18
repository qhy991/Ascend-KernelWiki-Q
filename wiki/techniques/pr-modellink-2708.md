---
id: technique-pr-modellink-2708
title: "PR Insight: Ascend/ModelLink #2708"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - qwen
  - checkpoint
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2708"
---

# PR Insight: Ascend/ModelLink #2708

**Title:** fix bug of sh of ckpt of qwen25

## Overview
This PR fixes a bug in the shell script for handling Qwen2.5 model checkpoints. The fix resolves issues with checkpoint saving, loading, or conversion for Qwen2.5 models.

## Technical Significance
Reliable checkpoint handling is essential for training workflows. This fix ensures that Qwen2.5 model checkpoints can be correctly managed on Ascend NPUs, enabling proper training state persistence and resumption.

## Related
- technique-operator-fusion