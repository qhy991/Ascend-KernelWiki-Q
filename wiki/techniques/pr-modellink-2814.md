---
id: technique-pr-modellink-2814
title: "PR Insight: Ascend/ModelLink #2814"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - pipeline-parallel
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2814"
---

# PR Insight: Ascend/ModelLink #2814

**Title:** [pytorch][bugfix]dualpipe mtp micro batch loss scale

## Overview
This PR fixes micro batch loss scaling for dual-pipeline multi-turn prediction (MTP) in the PyTorch backend. It ensures proper gradient scaling across micro batches.

## Technical Significance
Loss scaling is crucial for training stability, especially with mixed precision. This fix improves training stability for dual-pipeline MTP workflows on Ascend NPUs, preventing gradient issues during fine-tuning.

## Related
- `technique-pipeline-scheduling`
- `technique-distributed-training`