---
id: technique-pr-mindspeed-1187
title: "PR Insight: Ascend/MindSpeed #1187"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - noop
  - layernorm
  - recomputation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1187"
---

# PR Insight: Ascend/MindSpeed #1187

**Title:** 【BugFix】Noop Layer 和 Norm 重计算

## Overview
This PR fixes issues with Noop Layer and normalization (Norm) recomputation. Noop layers are pass-through layers used for alignment or structural purposes, while Norm recomputation helps save memory during training.

## Technical Significance
Proper handling of Noop layers and Norm recomputation is important for memory-efficient training on Ascend NPUs. This fix ensures these components work correctly with MindSpeed's optimization pipeline, preventing memory leaks or incorrect computations in models using layer normalization and structural layers.

## Related
- technique-memory-optimization
- kernel-layernorm