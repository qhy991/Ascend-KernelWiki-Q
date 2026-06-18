---
id: technique-pr-vllm-ascend-2602
title: "PR Insight: vllm-project/vllm-ascend #2602"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - disaggregation
  - layer-wise
  - mooncake
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2602"
---

# PR Insight: vllm-project/vllm-ascend #2602

**Title:** KVCache Transfer via Layer-wise Strategy in Disaggregation

## Overview
This PR implements a new KV cache connector for layer-wise KV transfer in disaggregated inference scenarios. It adds `mooncake_layerwise_connector.py` along with comprehensive test coverage and example implementations for layer-wise load balancing proxy servers.

## Technical Significance
The feature enables efficient KV cache transfer using a layer-wise strategy in disaggregated prefill/decode deployments. This allows users to leverage layer-wise features for better resource utilization and performance in distributed inference setups. The implementation includes extensive test coverage (1000+ lines) and integration with the existing mooncake connector infrastructure.

## Related
- `technique-kv-cache`
- `technique-disaggregation`
- `technique-layer-wise`