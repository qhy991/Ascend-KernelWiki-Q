---
id: technique-pr-vllm-ascend-997
title: "PR Insight: vllm-project/vllm-ascend #997"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multi-stream
  - shared-experts
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/997"
---

# PR Insight: vllm-project/vllm-ascend #997

**Title:** Support multistream of shared experts in FusedMoE

## Overview
This PR implements multi-stream parallelism for MoE layers with shared experts, overlapping shared expert computation with token dispatch and combine. When multi-stream is enabled, shared expert weights are force-replicated across all cards to avoid AllReduce operations.

## Technical Significance
Multi-stream parallelism significantly improves MoE performance by hiding communication latency. Overlapping shared expert computation (gate_up, act, down) with routed expert operations (dispatch, gate_up/act/down, combine) maximizes GPU utilization and reduces overall MoE layer latency.

## Related
- `kernel-moe`
- `technique-multi-stream`
- `technique-expert-parallel`