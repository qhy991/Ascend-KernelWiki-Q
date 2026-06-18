---
id: technique-pr-mindspeed-2587
title: "PR Insight: Ascend/MindSpeed #2587"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - atb
  - stream
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2587"
---

# PR Insight: Ascend/MindSpeed #2587

**Title:** fix stream of atb ops

## Overview
This PR fixes stream handling for ATB (Ascend Tensor Boost) operations in MindSpeed. The change ensures proper stream synchronization and execution order for ATB kernel calls.

## Technical Significance
ATB provides optimized kernels for Ascend hardware. Proper stream management is critical for correct execution, especially when operations have dependencies or require specific ordering. This fix prevents race conditions, synchronization issues, or incorrect results when using ATB operators.

## Related
- `technique-event-sync`
- `technique-instruction-queue`