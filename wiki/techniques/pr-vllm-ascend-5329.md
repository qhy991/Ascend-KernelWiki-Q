---
id: technique-pr-vllm-ascend-5329
title: "PR Insight: vllm-project/vllm-ascend #5329"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - all-reduce
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5329"
---

# PR Insight: vllm-project/vllm-ascend #5329

**Title:** [Feature] Enhance all-reduce skipping logic for MoE models in NPUModelRunner

## Overview
This PR enhances the all-reduce skipping logic for MoE models by skipping all_reduce when `max_num_batched_tokens` is below MC2's threshold, in addition to the existing `recompute_scheduler_enable` condition.

## Technical Significance
All-reduce operations are expensive in MoE models. Skipping them when batch sizes are small reduces communication overhead and improves throughput for small-batch inference scenarios on Ascend NPUs, complementing existing recompute-based optimization.

## Related
- technique-moe
- technique-hccl-optimization
- technique-communication-skipping