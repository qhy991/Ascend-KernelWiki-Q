---
id: technique-pr-modellink-2279
title: "PR Insight: Ascend/ModelLink #2279"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - training
  - qwen
  - rlhf
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2279"
---

# PR Insight: Ascend/ModelLink #2279

**Title:** R1-qwen复现 拒绝采样算法

## Overview
Implements rejection sampling algorithms for R1-qwen reproduction. This includes the algorithms and infrastructure needed for RLHF (Reinforcement Learning from Human Feedback) training workflows.

## Technical Significance
Enables RLHF training workflows for Qwen models by implementing rejection sampling. This is a key component for training high-quality instruction-following models using reinforcement learning techniques on Ascend hardware.

## Related
- technique-hccl-optimization
- technique-data-reuse