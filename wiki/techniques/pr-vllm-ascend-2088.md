---
id: technique-pr-vllm-ascend-2088
title: "PR Insight: vllm-project/vllm-ascend #2088"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - hccl
  - communication
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2088"
---

# PR Insight: vllm-project/vllm-ascend #2088

**Title:** [main][Feature]Moe alltoallv communication optimization for unquantized RL training sence

## Overview
This PR optimizes MoE alltoallv communication patterns for unquantized RL training scenarios and adds alltoallv support for DPO (Direct Preference Optimization). The optimization improves communication efficiency between expert groups in distributed MoE inference.

## Technical Significance
Optimized alltoallv communication reduces latency in MoE expert routing, which is critical for RL training workloads that require high throughput. The addition of DPO support expands the capability of vLLM-Ascend for advanced training scenarios on Ascend NPU.

## Related
- `technique-moe`
- `technique-hccl-optimization`
- `kernel-fused-moe`
- `technique-communication`