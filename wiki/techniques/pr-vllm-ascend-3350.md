---
id: technique-pr-vllm-ascend-3350
title: "PR Insight: vllm-project/vllm-ascend #3350"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - kv-cache
  - mooncake
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3350"
---

# PR Insight: vllm-project/vllm-ascend #3350

**Title:** Mooncake store use adxl inferface

## Overview
This PR mooncake store use adxl inferface. It modifies core implementation files including vllm_ascend/distributed/mooncake/config_data.py, vllm_ascend/distributed/mooncake/kv_transfer.py, vllm_ascend/distributed/mooncake/mooncake_store.py.

## Technical Significance
Integrates Mooncake storage using ADXL interface for efficient distributed KV cache management in prefill-decode separated architectures.

## Related
- `technique-kv-cache-paging`
- `technique-distributed-inference`
