---
id: technique-pr-modellink-2787
title: "PR Insight: Ascend/ModelLink #2787"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - checkpoint
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2787"
---

# PR Insight: Ascend/ModelLink #2787

**Title:** fix bug of ckpt in V3

## Overview
This PR fixes checkpoint-related bugs in version 3 of ModelLink. It addresses issues with saving and loading model checkpoints during training.

## Technical Significance
Checkpoint functionality is critical for long-running training on Ascend NPUs. This fix ensures reliable checkpoint saving and loading, preventing training interruptions and data loss during distributed training.

## Related
- `technique-distributed-training`