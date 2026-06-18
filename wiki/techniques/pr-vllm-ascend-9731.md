---
id: technique-pr-vllm-ascend-9731
title: "PR Insight: vllm-project/vllm-ascend #9731"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - ssd-offload
  - mooncake
  - storage
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9731"
---

# PR Insight: vllm-project/vllm-ascend #9731

**Title:** [Feature]Add Mooncake SSD offload with embedded client

## Overview
This PR adds Mooncake SSD offload Mode A (Embedded Real Client) support for the KV Pool MooncakeBackend used by AscendStoreConnector, enabling SSD-based KV cache eviction when DRAM is full. It aligns with Mooncake ssd-offload.md Step 3A specification.

## Technical Significance
Enables large-scale KV cache management by offloading evicted KV blocks to SSD when DRAM reaches high watermark (0.7). Performance testing with dual-machine PD separation, single-machine 8 cards, M2.7 model shows TTFT improvement from 22512.7ms to 10366.2ms (2.2× faster) and prefill throughput from 1457.2 to 3164.7 token/s (2.2× faster).

## Related
- `technique-kv-cache-paging`, `technique-distributed-kv`, `pattern-storage`