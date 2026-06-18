---
id: technique-pr-vllm-ascend-5149
title: "PR Insight: vllm-project/vllm-ascend #5149"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - prefix-caching
  - chunked-prefill
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5149"
---

# PR Insight: vllm-project/vllm-ascend #5149

**Title:** [E2E] add E2E for Prefix Caching cp & Chunked Prefill cp

## Overview
This PR adds end-to-end test cases for Prefix Caching with context parallelism (CP) and Chunked Prefill with context parallelism. The tests validate that these critical optimization features work correctly across multiple Ascend NPU devices.

## Technical Significance
Prefix caching and chunked prefill are essential for reducing compute cost and improving throughput for long-context workloads. Testing with context parallelism ensures these features work correctly in distributed scenarios where prefill stages are split across multiple Ascend NPUs.

## Related
- technique-prefix-caching
- technique-chunked-prefill
- technique-context-parallelism