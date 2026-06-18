---
id: technique-pr-vllm-ascend-7032
title: "PR Insight: vllm-project/vllm-ascend #7032"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - kv-pool
  - kv-transfer
  - connector
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7032"
---

# PR Insight: vllm-project/vllm-ascend #7032

**Title:** [P/D][KVPool]Mooncake Layerwise Connector supports kv_pool

## Overview
Creates and registers `AscendMultiConnector` to enable kv_pooling functionality in Mooncake Layerwise Connector. The implementation unregisters vLLM's original `MultiConnector` and replaces it with `AscendMultiConnector` during connector registration.

## Technical Significance
Enables efficient KV cache pooling for Mooncake Layerwise Connector by integrating custom connector implementation. Users can initialize `AscendMultiConnector` using the standard `MultiConnector` interface, providing seamless KV cache pooling capabilities.

## Related
- `technique-mooncake`, `technique-kv-pool`, `technique-kv-transfer`, `technique-connector`