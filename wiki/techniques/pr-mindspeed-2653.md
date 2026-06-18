---
id: technique-pr-mindspeed-2653
title: "PR Insight: Ascend/MindSpeed #2653"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - recompute
  - memory
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2653"
---

# PR Insight: Ascend/MindSpeed #2653

**Title:** fix recompute policy list overflow

## Overview
This PR fixes a list overflow bug in the recompute (gradient checkpointing) policy management. The error occurred when tracking which layers should be recomputed during backward pass, causing index errors or memory corruption.

## Technical Significance
Recompute is a memory-saving technique that trades computation for memory by recomputing forward activations during backward pass. Proper policy tracking is essential for correct gradient computation. This fix ensures robust handling of recompute policies across deep networks.

## Related
- `technique-double-buffering`
- `technique-pipeline-scheduling`