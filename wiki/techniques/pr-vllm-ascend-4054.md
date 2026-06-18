---
id: technique-pr-vllm-ascend-4054
title: "PR Insight: vllm-project/vllm-ascend #4054"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pipeline-parallel
  - mooncake-connector
  - kv-connector
  - disaggregation
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4054"
---

# PR Insight: vllm-project/vllm-ascend #4054

**Title:** mooncake connector support pipeline parallel & fix pp with flashcomm1

## Overview
This PR adds pipeline parallel support to mooncake connector for Prefill-Decode disaggregation and fixes bugs when enabling both pipeline parallel and flashcomm1. The changes include: (1) Mooncake connector support for PP in prefill (decode PP not yet supported), (2) Bug fixes for PP with flashcomm1, (3) Optimization of ascend-scheduler to support full batch in multiple pipeline stages, avoiding the issue where total batch_size across stages equals max_num_seq.

## Technical Significance
Pipeline parallel for prefill enables better resource utilization in PD disaggregated deployments. The scheduler optimization ensures all pipeline stages run with full batch_size, improving throughput. Fixing PP with flashcomm1 enables combining these optimizations for better performance. Mooncake connector support for PD disaggregation is critical for large-scale inference deployments.

## Related
- `technique-pipeline-parallel`, `technique-disaggregation`, `technique-mooncake-connector`, `pattern-scheduler-optimization`