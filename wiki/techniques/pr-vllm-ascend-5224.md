---
id: technique-pr-vllm-ascend-5224
title: "PR Insight: vllm-project/vllm-ascend #5224"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mooncake
  - pcp
  - dcp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5224"
---

# PR Insight: vllm-project/vllm-ascend #5224

**Title:** [feature] mooncake support pcp/dcp in common conditions

## Overview
This PR enables Mooncake to support complex PCP (Prefill-Context Parallelism) and DCP (Decode-Context Parallelism) configurations by establishing KV transfer mappings between prefill and decode nodes. It handles memory management by counting pull operations and properly freeing prefill rank KV cache blocks.

## Technical Significance
Supporting complex parallelism patterns like Prefill: TP8/PCP2DCP8 to Decode: TP8/DCP4/DP2 enables flexible deployment architectures for large-scale inference. Proper KV cache transfer and memory management prevent memory leaks and enable efficient resource utilization across Mooncake clusters.

## Related
- technique-kv-cache-paging
- technique-context-parallelism
- technique-hccl-optimization