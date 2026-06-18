---
id: technique-pr-mindspeed-1918
title: "PR Insight: Ascend/MindSpeed #1918"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - mc2
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1918"
---

# PR Insight: Ascend/MindSpeed #1918

**Title:** feat: mc2 frozen weight

## Overview
This PR adds support for frozen weights in MC2 (likely a parallelism or optimization mode). The feature allows certain model weights to remain frozen (not updated) during training while others are trainable.

## Technical Significance
Weight freezing is important for transfer learning, fine-tuning, and parameter-efficient training. Supporting frozen weights in MC2 enables more flexible training scenarios where only a subset of parameters need to be updated on Ascend NPUs.

## Related
- training-optimization
- parameter-efficient training