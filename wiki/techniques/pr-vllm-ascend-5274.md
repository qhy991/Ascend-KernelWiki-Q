---
id: technique-pr-vllm-ascend-5274
title: "PR Insight: vllm-project/vllm-ascend #5274"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - memory-optimization
  - mamba
  - contiguous
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5274"
---

# PR Insight: vllm-project/vllm-ascend #5274

**Title:** move contiguous in fused_sigmoid_gating_delta_rule_update to model_runner_v1

## Overview
This PR moves memory contiguity operations from the `fused_sigmoid_gating_delta_rule_update` operator to `model_runner_v1`. The change divides KV cache memory into two contiguous blocks (conv_state and ssm_state) to avoid expensive viewcopy operations when passing non-contiguous memory to operators.

## Technical Significance
Converting non-contiguous to contiguous memory during operator calls introduces expensive viewcopy operations that can degrade performance. By pre-allocating contiguous memory blocks in the model runner, this optimization reduces runtime overhead for Mamba/SLS (State Space Model) workloads on Ascend NPUs.

## Related
- technique-memory-optimization
- technique-mamba
- technique-contiguous-memory