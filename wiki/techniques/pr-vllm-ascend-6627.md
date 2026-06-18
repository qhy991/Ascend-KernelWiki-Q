---
id: technique-pr-vllm-ascend-6627
title: "PR Insight: vllm-project/vllm-ascend #6627"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - kv-transfer
  - mooncake
  - pcp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6627"
---

# PR Insight: vllm-project/vllm-ascend #6627

**Title:** [P/D][PCP] mooncake layerwise support pcp function

## Overview
This PR adds PCP (Prefill Context Parallelism) and DCP (Decode Context Parallelism) support to the Mooncake layerwise KV cache transfer mechanism. It enables more granular control and awareness of parallel configurations during distributed KV cache data transfer.

## Technical Significance
Extends Mooncake KV transfer capabilities to support context parallelism modes, enabling efficient distributed inference with both prefill and decode parallelism. The implementation provides better parallelism awareness and control in layerwise KV transfer operations.

## Related
- `technique-context-parallel`
- `technique-kv-cache-paging`