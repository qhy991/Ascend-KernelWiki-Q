---
id: technique-pr-vllm-ascend-2689
title: "PR Insight: vllm-project/vllm-ascend #2689"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - allgather
  - fused-op
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2689"
---

# PR Insight: vllm-project/vllm-ascend #2689

**Title:** allgather use fusedop.

## Overview
This PR optimizes allgather performance in MoE operations by replacing individual operators with fused operators. It uses `npu_moe_init_routing_v2` and `npu_moe_token_unpermute` to replace the previous three-operator sequence, improving TPS from 733.98 to 740.33 and reducing TTFT from 280.05 to 273.34.

## Technical Significance
The performance optimization achieves ~1% TPS improvement and ~2.4% TTFT reduction by consolidating MoE routing operations into fused operators. By replacing the three-step sequence (npu_moe_init_routing, npu_moe_compute_expert_tokens, npu_moe_finalize_routing) with two fused operators, the PR reduces operator overhead and improves memory locality.

## Related
- `technique-moe`
- `technique-allgather`
- `technique-operator-fusion`