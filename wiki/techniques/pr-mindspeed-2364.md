---
id: technique-pr-mindspeed-2364
title: "PR Insight: Ascend/MindSpeed #2364"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - swiglu
  - fused
  - recompute
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2364"
---

# PR Insight: Ascend/MindSpeed #2364

**Title:** add --use-fused-swiglu;  fix: RecomputeMethod

## Overview
This PR adds a --use-fused-swiglu flag and fixes RecomputeMethod. SwiGLU is an activation function commonly used in transformer models, and fusing it improves performance.

## Technical Significance
Enables fused SwiGLU activation for better performance and fixes recompute method issues. Fused activations reduce kernel launch overhead, and the recompute fix ensures memory optimization works correctly.

## Related
- `kernel-elementwise-ascendc`
- `technique-operator-fusion`
- `technique-recompute`
- `technique-swiglu`