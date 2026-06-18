---
id: technique-pr-mindspeed-2343
title: "PR Insight: Ascend/MindSpeed #2343"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - norm
  - recompute
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2343"
---

# PR Insight: Ascend/MindSpeed #2343

**Title:** fix bug for norm recompute

## Overview
This PR fixes a bug in the norm recompute functionality within MindSpeed. Norm operations (LayerNorm/RMSNorm) are critical in transformer architectures for stable training. The fix addresses issues that likely occur during recompute (activation recomputation), which is a memory optimization technique used during training to trade compute for memory.

## Technical Significance
Norm recompute bugs can cause numerical instability or incorrect gradients, leading to training divergence or incorrect results. This fix ensures that norm operations are correctly recomputed when activations are not stored, which is essential for memory-efficient training strategies like selective activation recomputation.

## Related
- `technique-activation-recompute`
- `kernel-layernorm`
- `pattern-memory-optimization`