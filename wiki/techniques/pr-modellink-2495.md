---
id: technique-pr-modellink-2495
title: "PR Insight: Ascend/ModelLink #2495"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - checkpoint
  - bugfix
  - script
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2495"
---

# PR Insight: Ascend/ModelLink #2495

**Title:** 修复部分脚本缺少ckpt_load,ckpt_save的问题

## Overview
This PR fixes missing ckpt_load and ckpt_save functionality in some scripts. Checkpoint loading and saving are essential for training resilience and model deployment.

## Technical Significance
Adding checkpoint support to scripts enables proper training interruption recovery and model saving for deployment on Ascend hardware. This prevents loss of training progress.

## Related
- checkpoint save/load
- training resilience