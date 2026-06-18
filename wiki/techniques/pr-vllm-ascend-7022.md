---
id: technique-pr-vllm-ascend-7022
title: "PR Insight: vllm-project/vllm-ascend #7022"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - hybrid-attention
  - kv-cache
  - multi-group
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7022"
---

# PR Insight: vllm-project/vllm-ascend #7022

**Title:** [P/D]Mooncake Layerwise Connector supports hybrid attention manager with multiple kvcache groups

## Overview
Extends Mooncake Layerwise Connector to support hybrid attention manager with multiple KV cache groups. This enables more flexible KV cache management for parallel disaggregated scenarios with varying attention mechanisms.

## Technical Significance
Improves flexibility of Mooncake Layerwise Connector by supporting multiple KV cache groups with different attention patterns. This enables better resource utilization and more efficient distributed inference in hybrid attention scenarios.

## Related
- `technique-mooncake`, `technique-hybrid-attention`, `technique-kv-cache-groups`, `technique-layerwise-connector`