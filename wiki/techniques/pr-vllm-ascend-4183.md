---
id: technique-pr-vllm-ascend-4183
title: "PR Insight: vllm-project/vllm-ascend #4183"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake-connector
  - pcp
  - dcp
  - kv-connector
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4183"
---

# PR Insight: vllm-project/vllm-ascend #4183

**Title:** [feature] Mooncake_connector support pcp/dcp

## Overview
This PR adds PCP (Prefill Context Parallel) and DCP (Decode Context Parallel) support to mooncake connector. The changes enable mooncake connector to work with context parallelism, expanding its capabilities for distributed inference scenarios with KV cache sharing across context parallel dimensions.

## Technical Significance
Adding PCP/DCP support to mooncake connector enables context parallelism in PD disaggregated deployments. This allows better resource utilization and performance by sharing KV cache across context parallel dimensions while maintaining the benefits of the mooncake connector for distributed inference.

## Related
- `technique-mooncake-connector`, `technique-context-parallel`, `technique-disaggregation`, `pattern-distributed-inference`