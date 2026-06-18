---
id: technique-pr-vllm-ascend-2472
title: "PR Insight: vllm-project/vllm-ascend #2472"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - aclgraph
  - resources
  - stream-management
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2472"
---

# PR Insight: vllm-project/vllm-ascend #2472

**Title:** [Fix] fix resources limit error when apply speculative decoding and aclgraph

## Overview
This PR fixes a resource limit error that occurred when both speculative decoding and ACL Graph were applied with default `cudagraph_capture_sizes` values. The fix updates resource management logic in `vllm_ascend/utils.py` to properly handle the combined resource requirements.

## Technical Significance
This fix prevents out-of-stream-resource errors when combining speculative decoding with ACL Graph mode. The proper resource management ensures that both features can be used together without exceeding available stream resources, which is critical for production deployments using both optimizations.

## Related
- `technique-speculative-decoding`, `technique-aclgraph-integration`, `technique-resource-management`, `technique-stream-allocation`