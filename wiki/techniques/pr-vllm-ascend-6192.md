---
id: technique-pr-vllm-ascend-6192
title: "PR Insight: vllm-project/vllm-ascend #6192"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - eagle3
  - dp-allreduce
  - data-parallel
  - moe
  - speculative-decoding
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6192"
---

# PR Insight: vllm-project/vllm-ascend #6192

**Title:** [Eagle3]enhance skipping dp allreduce and add it into eagle proposer

## Overview
This PR enhances data parallel allreduce skipping logic and integrates it into the Eagle3 proposer for improved speculative decoding performance. The implementation enhances `_skip_all_reduce_across_dp_group` to skip all CPU DP allreduce operations for dense models and adds this optimization to the eagle proposer. This enables models like Qwen3-235B to support Eagle3 spec decode even with `dp_size > 1` configurations common in PD disaggregation scenarios.

## Technical Significance
This optimization significantly improves Eagle3 speculative decoding performance by eliminating unnecessary CPU-side allreduce operations. In PD disaggregation scenarios with `dp_size > 1`, the original implementation required `set_forward_context` to call a CPU DP allreduce to retrieve `num_tokens_across_dp` on all cases, causing significant overhead. By enhancing the skipping logic to apply to dense models and integrating it into the eagle proposer, the optimization eliminates this bottleneck while maintaining correctness. This enables efficient Eagle3 speculative decoding for large MoE models that typically use data parallel scaling in production deployments.

## Related
- `technique-speculative-decoding`, `technique-eagle3`, `technique-data-parallel`, `technique-allreduce`, `technique-moe`