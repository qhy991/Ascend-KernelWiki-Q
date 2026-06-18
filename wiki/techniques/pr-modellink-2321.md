---
id: technique-pr-modellink-2321
title: "PR Insight: Ascend/ModelLink #2321"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - ppo
  - rlhf
  - distributed-training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2321"
---

# PR Insight: Ascend/ModelLink #2321

**Title:** 【TRL PPO】supporr SP, support EP, support rollout batch size and log bug fix

## Overview
This PR adds support for Sequence Parallelism (SP) and Expert Parallelism (EP) to TRL PPO training, adds rollout batch size configuration, and fixes logging bugs. The enhancements improve PPO training scalability and configurability on Ascend hardware.

## Technical Significance
PPO for RLHF requires complex compute patterns including policy/value network forward passes, reward computation, and policy gradient updates. Adding SP and EP enables scaling PPO training to larger models and batch sizes by distributing sequences and experts across multiple NPUs. Rollout batch size configuration allows tuning memory usage and throughput. These improvements make large-scale RLHF training feasible on Ascend clusters for model alignment tasks.

## Related
- `technique-rlhf-training`
- `technique-sequence-parallelism`
- `technique-expert-parallelism`
- `technique-hccl-optimization`