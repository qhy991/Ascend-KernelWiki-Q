---
id: technique-pr-vllm-ascend-3811
title: "PR Insight: vllm-project/vllm-ascend #3811"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - shared-expert
  - dp
  - deepseek-mtp
  - reduce-scatter
  - all-gather
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3811"
---

# PR Insight: vllm-project/vllm-ascend #3811

**Title:** [Feat] shared expert dp for deepseek_mtp

## Overview
This PR enables shared expert data parallelism (DP) for DeepSeek-MTP models. Previously, shared expert DP was removed due to coupling with torchair and the removal of deepseek_mtp. The implementation performs reduce-scatter on deepseek_mtp input in `mtp_proposer.py` to match input_embedding dimensions, then all-gathers on MTP output. Benchmark results show TPOT improvement from 48ms to 45.4ms and average TPS per rank from 117.6 to 126.1.

## Technical Significance
Shared expert DP reduces computation redundancy by parallelizing shared expert layers across data parallel ranks. The re-implementation for MTP spec decode requires careful dimension management through reduce-scatter/all-gather patterns. The ~7% throughput improvement demonstrates the value of this optimization for large MoE models.

## Related
- `technique-moe`
- `technique-shared-expert`
- `technique-mtp`
- `technique-data-parallelism`