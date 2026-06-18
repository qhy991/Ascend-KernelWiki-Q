---
id: technique-pr-vllm-ascend-1296
title: "PR Insight: vllm-project/vllm-ascend #1296"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - prefill
  - kv-cache
  - distributed
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1296"
---

# PR Insight: vllm-project/vllm-ascend #1296

**Title:** Disaggregate prefill for kv cache register style （merge into v0.9.1-dev）

## Overview
This PR implements disaggregated prefill for KV cache register style, enabling prefill and decode phases to run on separate devices. It includes distributed connectors, scheduler patches, and comprehensive test coverage.

## Technical Significance
Enables scaling of prefill and decode workloads across different NPU instances by separating KV cache management. The implementation adds `llmdatadist_c_mgr_connector` for distributed coordination, updates attention and MLA V1 components for disaggregated operations, and provides full workflow examples. This is critical for production deployments where prefill and decode have different resource requirements.

## Related
- `technique-disaggregated-prefill`
- `technique-kv-cache-paging`
- `kernel-attention`