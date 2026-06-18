---
id: technique-pr-vllm-ascend-1644
title: "PR Insight: vllm-project/vllm-ascend #1644"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - disaggregated-prefill
  - allreduce
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1644"
---

# PR Insight: vllm-project/vllm-ascend #1644

**Title:** [0.9.1][PD][Perf] Avoid performing cpu all_reduce in disaggregated-prefill scenario

## Overview
This PR optimizes disaggregated prefill by avoiding CPU-side all_reduce operations, reducing synchronization overhead.

## Technical Significance
Improves disaggregated prefill performance by keeping all-reduce operations on NPU instead of bouncing through CPU. This eliminates costly host-device synchronization and improves throughput for prefill-decode separated deployments.

## Related
- `technique-disaggregated-prefill`
- `technique-hccl-optimization`
- `technique-npu-offload`