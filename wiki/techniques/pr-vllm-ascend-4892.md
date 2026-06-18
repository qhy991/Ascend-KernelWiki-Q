---
id: technique-pr-vllm-ascend-4892
title: "PR Insight: vllm-project/vllm-ascend #4892"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - kv-transfer
  - pipeline-parallelism
  - mooncake
  - layer-partition
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4892"
---

# PR Insight: vllm-project/vllm-ascend #4892

**Title:** [Bugfix] support mtp kv transfer and pp partition by hand in kv transfer

## Overview
This PR fixes two issues with Mooncake connector when PP and MTP are enabled: (1) MTP layer KV caches were not being transferred, causing decreased accept ratio. The fix adds MTP layer indices for the last PP stage after calculating end_layer in transfer_kv_cache. (2) With MTP, default PP layer division may cause imbalance. The fix adds pp_layer_partition config in kv_connector_extra_config so decode nodes can acquire prefill node partition info.

## Technical Significance
Enables proper KV cache transfer for MTP in Mooncake and supports manual PP layer partitioning to balance workload. This ensures high acceptance ratios in speculative decoding and efficient resource utilization across pipeline stages.

## Related
- `technique-kv-cache-transfer`
- `technique-pipeline-parallelism`
- `technique-mtp`
- `kernel-mooncake-connector`