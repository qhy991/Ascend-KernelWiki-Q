---
id: technique-pr-vllm-ascend-6729
title: "PR Insight: vllm-project/vllm-ascend #6729"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - memory-optimization
  - hccl
  - communication
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6729"
---

# PR Insight: vllm-project/vllm-ascend #6729

**Title:** [EPLB] Reduce the memory used for heat aggregation

## Overview
This PR reduces memory consumption in EPLB heat aggregation by creating a separate small communication domain instead of using dist.all_gather directly. The change reduces memory from 2x HCCL_BUFFSIZE to less than 1MB since the actual memory required for hotspot aggregation is small.

## Technical Significance
Significantly reduces memory footprint of EPLB operations by avoiding unnecessary large buffer allocations for small aggregation operations. The dedicated communication domain optimization prevents memory waste while maintaining the required functionality.

## Related
- `technique-kv-cache-paging`
- `technique-hccl-optimization`