---
id: technique-pr-vllm-ascend-6295
title: "PR Insight: vllm-project/vllm-ascend #6295"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-transfer
  - cache-load
  - mooncake
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6295"
---

# PR Insight: vllm-project/vllm-ascend #6295

**Title:** [P/D] Using the cache load operator to replace the index select operator.

## Overview
This PR replaces the index select operator with the cache load operator in KV transfer operations for Mooncake layerwise connector. The change was made in `vllm_ascend/distributed/kv_transfer/kv_p2p/mooncake_layerwise_connector.py`.

## Technical Significance
Using the cache load operator instead of index select provides better performance for KV cache access in distributed inference scenarios. The cache load operator is optimized for the Ascend hardware and reduces overhead in prefill/decode disaggregated pipelines.

## Related
- `technique-kv-cache`
- `technique-kv-transfer`
- `technique-mooncake`
- `technique-cache-load`