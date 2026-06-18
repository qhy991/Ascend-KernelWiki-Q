---
id: technique-pr-mindspeed-1386
title: "PR Insight: Ascend/MindSpeed #1386"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - smart-swap
  - memory
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1386"
---

# PR Insight: Ascend/MindSpeed #1386

**Title:** add feature smart swap

## Overview
This PR adds the smart swap feature to MindSpeed. Smart swap intelligently manages memory by swapping data between device memory and host memory to handle models larger than available device memory.

## Technical Significance
Smart swap enables training of very large models that don't fit entirely in device memory. The feature improves memory utilization and allows scaling to larger model sizes on Ascend NPUs by strategically offloading less frequently accessed data.

## Related
- memory-optimization
- data-reuse
- unified-buffer management