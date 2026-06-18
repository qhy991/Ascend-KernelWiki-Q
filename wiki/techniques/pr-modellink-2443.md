---
id: technique-pr-modellink-2443
title: "PR Insight: Ascend/ModelLink #2443"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - distributed
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2443"
---

# PR Insight: Ascend/ModelLink #2443

**Title:** add ray stop

## Overview
This PR adds Ray distributed framework stop functionality, improving cluster management and resource cleanup when training jobs complete or are interrupted.

## Technical Significance
Proper resource management in distributed training environments prevents resource leaks and ensures clean shutdown of distributed jobs, which is critical for large-scale multi-node training on Ascend clusters.

## Related
- `technique-distributed-training` / `technique-ray` / `technique-cluster-management`