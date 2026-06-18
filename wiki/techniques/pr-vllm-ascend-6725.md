---
id: technique-pr-vllm-ascend-6725
title: "PR Insight: vllm-project/vllm-ascend #6725"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - recurrent-gated-delta-rule
  - qwen3-next
  - ascendc
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6725"
---

# PR Insight: vllm-project/vllm-ascend #6725

**Title:** Add Ascend Ops recurrent_gated_delta_rule

## Overview
This PR migrates the recurrent_gated_delta_rule operations from Triton implementation to AscendC for better performance. The change applies to Qwen3-Next model inference.

## Technical Significance
Improves performance of recurrent_gated_delta_rule operations by leveraging AscendC optimizations instead of Triton. The AscendC implementation provides better hardware utilization and lower latency for these specialized operations.

## Related
- `kernel-elementwise`