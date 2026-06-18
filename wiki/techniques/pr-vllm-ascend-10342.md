---
id: technique-pr-vllm-ascend-10342
title: "PR Insight: vllm-ascend #10342"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - memory
  - kv-cache
  - mooncake
  - deepseek
  - architecture
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10342"
---

# PR Insight: vllm-ascend #10342 - Mooncake Connector Support for DeepSeek V4

## Overview
This feature PR (`[Feature] Mooncake connectot support dsv4`) adds support within the Mooncake connector for DeepSeek V4 and hybrid KV cache scenarios on Ascend platforms.

## Architecture and Technical Details
DeepSeek V4 introduces complex mixed KV cache layouts that require advanced memory management and cache transfer strategies. The new layouts specifically supported by this PR include:
* **Attention KV:** Standard key-value cache used for standard attention layers.
* **Compressed KV:** Memory-optimized representations, crucial for reducing memory bandwidth and footprint in large sequence scenarios.
* **Sliding-Window KV:** Localized KV cache optimizations that restrict attention to recent context windows.
* **Mamba/State Cache Groups:** State caching structures needed for hybrid architectures that integrate Mamba/RNN components with traditional attention.

The update ensures the Mooncake transfer logic can effectively handle these heterogeneous caching formats in a unified system, overcoming the limitations of previous architectures that only anticipated standard transformer KV cache structures.

## Impact
* **DeepSeek V4 Support:** Essential memory logistics required to execute DeepSeek V4 efficiently on Ascend NPU architectures.
* **Hybrid Model Capabilities:** Expands the ecosystem's ability to run models utilizing both standard attention mechanisms and state-based architectures (like Mamba) simultaneously.
* **Memory Efficiency:** Improves handling of compressed and sliding-window cache variants over distributed KVCache endpoints.
