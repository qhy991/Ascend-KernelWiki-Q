---
id: technique-pr-modellink-2671
title: "PR Insight: Ascend/ModelLink #2671"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2671"
---

# PR Insight: Ascend/ModelLink #2671

**Title:** fix pipeline mistakes

## Overview
This PR fixes mistakes in the pipeline parallelism implementation of ModelLink. Pipeline parallelism is a technique for training large models across multiple devices by splitting the model into stages, and this fix addresses issues in that implementation on Ascend hardware.

## Technical Significance
Pipeline parallelism is essential for training models that don't fit on a single device. Fixing pipeline mistakes ensures reliable and efficient distributed training on Ascend NPUs, enabling users to train larger models with correct gradient flow and synchronization.

## Related
- technique-pipeline-scheduling
- technique-hccl-optimization