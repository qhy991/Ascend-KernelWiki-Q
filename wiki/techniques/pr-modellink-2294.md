---
id: technique-pr-modellink-2294
title: "PR Insight: Ascend/ModelLink #2294"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - training
  - qwen
  - rlhf
  - dataset
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2294"
---

# PR Insight: Ascend/ModelLink #2294

**Title:** 【R1-qwen复现 Part1】混合reward+blended dataset

## Overview
Implements mixed reward and blended dataset functionality for R1-qwen reproduction Part 1. This includes the data processing and reward model integration needed for RLHF training.

## Technical Significance
Enhances RLHF training capabilities for Qwen models by supporting mixed reward signals and blended datasets. This improves the quality and diversity of training data for reinforcement learning workflows on Ascend hardware.

## Related
- technique-hccl-optimization
- technique-data-reuse