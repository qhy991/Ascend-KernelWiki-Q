---
id: technique-pr-modellink-2649
title: "PR Insight: Ascend/ModelLink #2649"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2649"
---

# PR Insight: Ascend/ModelLink #2649

**Title:** fix pipeline mistakes

## Overview
This PR fixes mistakes in the pipeline parallelism implementation of ModelLink. The changes correct issues in pipeline stage management, gradient synchronization, or scheduling during distributed training on Ascend hardware.

## Technical Significance
Pipeline parallelism is a key technique for training large models across multiple devices. Fixing pipeline mistakes ensures correct and efficient distributed training on Ascend NPUs, enabling users to successfully train models that don't fit on a single device.

## Related
- technique-pipeline-scheduling
- technique-hccl-optimization