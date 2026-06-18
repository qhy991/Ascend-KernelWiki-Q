---
id: technique-pr-mindspeed-2610
title: "PR Insight: Ascend/MindSpeed #2610"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - sp
  - alignment
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2610"
---

# PR Insight: Ascend/MindSpeed #2610

**Title:** bugfix:fix unaligned sp

## Overview
This PR fixes an unaligned SP (likely sequence parallelism or sequence packing) issue. The bug caused errors when tensor sequences were not properly aligned, leading to incorrect results or crashes during training.

## Technical Significance
Proper sequence alignment is critical for efficient memory access and correct computation in sequence parallelism. Unaligned sequences can cause performance degradation or numerical errors. This fix ensures that sequence dimensions are correctly handled across parallel devices.

## Related
- `technique-nz-tiling`
- `technique-hccl-optimization`