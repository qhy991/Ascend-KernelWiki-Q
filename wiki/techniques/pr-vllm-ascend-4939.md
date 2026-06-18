---
id: technique-pr-vllm-ascend-4939
title: "PR Insight: vllm-project/vllm-ascend #4939"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - allreduce
  - precision
  - verl
  - rl
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4939"
---

# PR Insight: vllm-project/vllm-ascend #4939

**Title:** [Bugfix] Fix matmul allreduce precision issue by using original weight

## Overview
This PR fixes precision issues in matmul allreduce operations under Verl reinforcement learning scenarios. The key changes are: (1) Remove custom class member self.weight_t in vllm_ascend/ops/linear_op.py, and (2) Adjust npu_mm_all_reduce_base operator input logic to directly fetch weight parameters from the model's nn.Parameters instead of using pre-created Tensors.

## Technical Significance
Fixes a critical precision issue caused by unsynchronized parameter copies. In Verl RL scenarios, parameter synchronization between training and inference may change nn.Parameter memory addresses, causing unsynchronized extra Tensors to reference old memory. Using the original parameters directly ensures correct computation.

## Related
- `kernel-matmul`
- `kernel-allreduce`
- `kernel-npu-mm-all-reduce`
- `technique-verl-integration`