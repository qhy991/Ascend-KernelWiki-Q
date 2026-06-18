---
id: technique-pr-modellink-2377
title: "PR Insight: Ascend/ModelLink #2377"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - tro
  - ppo
  - rlhf
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2377"
---

# PR Insight: Ascend/ModelLink #2377

**Title:** tro ppo 资料修改

## Overview
This PR updates documentation and configuration for TRO (Technical Reference Optimization) PPO (Proximal Policy Optimization) training workflows. The changes improve the user-facing materials for reinforcement learning from human feedback (RLHF) implementations on Ascend hardware.

## Technical Significance
PPO training for RLHF requires specialized compute patterns including policy/value network forward passes, reward computation, and policy gradient updates. These are memory-intensive and communication-heavy operations that benefit from Ascend's collective communication primitives (HCCL). Documentation updates ensure users can correctly configure PPO training with proper distributed setup, memory management, and performance tuning for large language model alignment tasks.

## Related
- `technique-rlhf-training`
- `technique-hccl-optimization`