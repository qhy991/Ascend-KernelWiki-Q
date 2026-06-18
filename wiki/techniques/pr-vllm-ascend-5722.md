---
id: technique-pr-vllm-ascend-5722
title: "PR Insight: vllm-project/vllm-ascend #5722"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mooncake
  - kv-connector
  - sparse-attention
  - deepseek-v3
  - pd-disaggregation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5722"
---

# PR Insight: vllm-project/vllm-ascend #5722

**Title:** [P/D] layerwise connector supports DeepSeek-V3.2 sparse attention && Distribute transfer tasks to redundant kv_head cards

## Overview
This PR enhances the mooncake layerwise KV cache connector with two key capabilities: support for DeepSeek-V3.2 sparse attention patterns, and intelligent task distribution to redundant kv_head cards. The implementation updates `mooncake_layerwise_connector.py` and `sfa_v1.py` to handle sparse attention patterns and load-balance transfer tasks across available KV head cards for improved resource utilization in PD (prefill-decode) disaggregation scenarios.

## Technical Significance
This optimization improves prefill-decode disaggregation efficiency by enabling sparse attention support for DeepSeek-V3.2 and distributing KV cache transfer tasks across redundant hardware resources. The key technique is load balancing transfer tasks to leverage all available kv_head cards rather than a subset, which reduces contention and improves throughput in PD scenarios. The sparse attention support is specifically designed for DeepSeek-V3.2's attention patterns, enabling efficient chunked context handling with proper alignment to the model's sparse structure.

## Related
- `technique-kv-cache-paging`, `technique-pd-disaggregation`, `technique-sparse-attention`, `technique-hccl-optimization`