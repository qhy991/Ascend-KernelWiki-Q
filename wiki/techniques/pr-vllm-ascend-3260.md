---
id: technique-pr-vllm-ascend-3260
title: "PR Insight: vllm-project/vllm-ascend #3260"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - prefill
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3260"
---

# PR Insight: vllm-project/vllm-ascend #3260

**Title:** support cp&dcp

## Overview
This PR adds the Prefill Context Parallelism (PCP) feature, which corresponds to DCP. For specific implementation details, please refer to the RFC https://github.com/vllm-project/vllm/issues/25749.

## Technical Significance
Implements Prefill Context Parallelism (PCP) and Decode Context Parallelism (DCP) features for scaling long-sequence processing across multiple Ascend NPU devices.

## Related
- `hw-cube-unit`
- `technique-kv-cache-paging`
- `technique-hccl-optimization`
