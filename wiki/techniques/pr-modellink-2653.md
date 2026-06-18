---
id: technique-pr-modellink-2653
title: "PR Insight: Ascend/ModelLink #2653"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - training
  - pipeline
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2653"
---

# PR Insight: Ascend/ModelLink #2653

**Title:** fix pipeline mistakes

## Overview
This PR fixes mistakes in the pipeline parallelism implementation of ModelLink. The changes address issues in how pipeline stages are managed, synchronized, or scheduled during distributed training on Ascend hardware.

## Technical Significance
Pipeline parallelism is essential for training models larger than what fits on a single device. Correcting pipeline mistakes ensures reliable distributed training with proper gradient flow and synchronization on Ascend NPUs, enabling users to train larger models successfully.

## Related
- technique-pipeline-scheduling
- technique-hccl-optimization