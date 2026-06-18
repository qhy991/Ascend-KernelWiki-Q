---
id: technique-pr-vllm-ascend-9090
title: "PR Insight: vllm-project/vllm-ascend #9090"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - paged-attention
  - operator-abstraction
  - a5
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9090"
---

# PR Insight: vllm-project/vllm-ascend #9090

**Title:** [Feature] A5 npu_gather_pa_kv_cache operator adaptation for pcp

## Overview
This PR adapts the `npu_gather_pa_kv_cache` operator for the A5 architecture in the paged context parallel (PCP) path. It replaces direct `torch_npu.atb.npu_paged_cache_load` calls in `_load_kv_for_chunk` with `DeviceOperator.kv_cache_load`, enabling the KV cache loading path to go through the device operator abstraction layer.

## Technical Significance
The abstraction of KV cache loading through `DeviceOperator.kv_cache_load` provides better device portability and consistent operator interfaces across different Ascend architectures. This adaptation enables efficient key-value data retrieval from the paged KV cache for A5 NPUs in context-parallel inference scenarios, improving code maintainability and enabling future hardware support.

## Related
- `technique-kv-cache-paging`, `kernel-attention-ascendc`, `technique-context-parallel`