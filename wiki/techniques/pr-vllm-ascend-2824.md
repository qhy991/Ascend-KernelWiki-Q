---
id: technique-pr-vllm-ascend-2824
title: "PR Insight: vllm-project/vllm-ascend #2824"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-connector
  - mooncake
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2824"
---

# PR Insight: vllm-project/vllm-ascend #2824

**Title:** fix mooncake connector adxl hostname usage

## Overview
This PR fixes the hostname usage in the Mooncake connector's ADXL integration, correcting how the connector resolves and uses hostnames for distributed inference scenarios.

## Technical Significance
Bug fix for the Mooncake KV cache connector, which is important for distributed inference deployments using external KV cache services. Correct hostname handling is critical for proper communication between inference workers and the Mooncake KV cache service, preventing connection failures or routing issues in distributed inference setups.

## Related
- `technique-kv-cache-paging`, `technique-distributed-inference`