---
id: technique-pr-vllm-ascend-2006
title: "PR Insight: vllm-project/vllm-ascend #2006"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - sequence-parallel
  - moe
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2006"
---

# PR Insight: vllm-project/vllm-ascend #2006

**Title:** 【091dev】 Qwen3 moe support sp

## Overview
This PR adds Sequence Parallelism (SP) support for Qwen3 MoE models by replacing AllReduce operations with Reduce-Scatter and AllGather in scenarios like AlltoAll, AlltoAllv, and MC2. This optimization is enabled during the prefill phase and provides computational benefits in norm operations while saving one AllGather communication.

## Technical Significance
Sequence Parallelism delivers 5%-10% performance improvements for Qwen3 MoE in long-sequence scenarios (16k-25k tokens). By optimizing communication patterns, this PR reduces synchronization overhead and improves computational efficiency on Ascend NPUs, making it valuable for production inference with long-context workloads.

## Related
- `technique-sequence-parallel`
- `technique-moe`
- `technique-qwen3`
- `technique-hccl-optimization`