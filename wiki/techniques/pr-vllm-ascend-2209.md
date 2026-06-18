---
id: technique-pr-vllm-ascend-2209
title: "PR Insight: vllm-project/vllm-ascend #2209"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - sequence-parallelism
  - alltoall
  - mc2
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2209"
---

# PR Insight: vllm-project/vllm-ascend #2209

**Title:** 【main】SP For Qwen3 MoE

## Overview
This PR adds Sequence Parallelism (SP) support for Qwen3 MoE models. In AlltoAll, AlltoAllv, and MC2 scenarios, replacing AllReduce with Reduce-Scatter and AllGather achieves computational benefits in norm operations while saving one AllGather communication. The implementation adds 120 lines to `vllm_ascend/ops/sequence_parallel.py` and 120 lines to `vllm_ascend/models/qwen3_moe.py`, enabled via compilation config `enable_sequence_parallelism: True`.

## Technical Significance
This optimization delivers 5-10% performance improvements in long-sequence scenarios (16k-25k tokens) by leveraging sequence parallelism to replace expensive AllReduce operations with more efficient Reduce-Scatter and AllGather patterns. The feature is enabled during the P-phase and provides notable gains for workloads with long contexts.

## Related
- `kernel-fused-moe-ascendc`, `technique-sequence-parallelism`, `kernel-layernorm-ascendc`, `technique-hccl-optimization`