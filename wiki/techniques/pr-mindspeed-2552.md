---
id: technique-pr-mindspeed-2552
title: "PR Insight: Ascend/MindSpeed #2552"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - hccl
  - communication
  - buffer
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2552"
---

# PR Insight: Ascend/MindSpeed #2552

**Title:** [fix bug] hccl_buff cannt be zero

## Overview
This PR fixes a bug where the HCCL (Huawei Collective Communication Library) buffer size could incorrectly be set to zero. The issue could cause communication failures or crashes during distributed training.

## Technical Significance
HCCL buffers must have non-zero size for collective communication operations to work correctly. This fix ensures proper buffer allocation and prevents invalid buffer configurations that would cause runtime errors in distributed training scenarios.

## Related
- `technique-hccl-optimization`
- `technique-double-buffering`