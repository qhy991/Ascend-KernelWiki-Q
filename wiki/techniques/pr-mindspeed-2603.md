---
id: technique-pr-mindspeed-2603
title: "PR Insight: Ascend/MindSpeed #2603"
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
  - "https://gitee.com/ascend/MindSpeed/pulls/2603"
---

# PR Insight: Ascend/MindSpeed #2603

**Title:** bugfix: Fix unaligned SP bug

## Overview
This PR fixes an unaligned SP (Sequence Parallelism) bug. The issue caused failures or incorrect results when tensor dimensions were not properly aligned for sequence-parallel computation across devices.

## Technical Significance
Sequence parallelism splits sequence dimensions across devices to reduce memory footprint and improve throughput. Proper alignment is essential for correct communication and computation. This fix ensures that sequence tensors are correctly padded or reshaped to meet alignment requirements.

## Related
- `technique-nz-tiling`
- `technique-hccl-optimization`