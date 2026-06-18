---
id: technique-pr-modellink-2359
title: "PR Insight: Ascend/ModelLink #2359"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - ppo
  - llama
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2359"
---

# PR Insight: Ascend/ModelLink #2359

**Title:** shell bug fix and data_convert script for llama ppo

## Overview
This PR fixes shell script bugs and adds data conversion scripts for LLaMA PPO (Proximal Policy Optimization) training. The changes enable proper RLHF fine-tuning workflows for LLaMA-based models on Ascend hardware.

## Technical Significance
PPO training requires specialized data pipelines for reward modeling, generation sampling, and policy updates. The data conversion scripts handle transformation between different data formats needed for reward computation and policy gradient computation. This integration enables efficient RLHF training for LLaMA models on Ascend NPUs, with proper support for distributed reward computation and policy/value network training across multiple nodes.

## Related
- `technique-rlhf-training`
- `technique-data-preprocessing`