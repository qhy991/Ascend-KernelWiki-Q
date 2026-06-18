---
id: technique-pr-vllm-ascend-2129
title: "PR Insight: vllm-project/vllm-ascend #2129"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - allreduce
  - cpu
  - d-node
  - prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2129"
---

# PR Insight: vllm-project/vllm-ascend #2129

**Title:** [bugfix] add with_prefill cpu allreduce to handle D-node recomputation situations

## Overview
This PR adds CPU AllReduce support for with-prefill scenarios to handle D-node (decode node) recomputation situations in disaggregated inference setups. The implementation modifies `vllm_ascend/models/deepseek_v2.py` and `vllm_ascend/worker/model_runner_v1.py` to enable CPU-based allreduce when GPU allreduce isn't available or fails.

## Technical Significance
This fix addresses stability issues in disaggregated inference where the D-node needs to recompute certain operations. By falling back to CPU allreduce when GPU-based communication fails, the system maintains forward progress. Benchmark results show improvements across GSM8K, LiveCodeBench, and vLLM benchmark workloads, demonstrating the importance of robust communication fallback mechanisms in distributed inference.

## Related
- `technique-hccl-optimization`, `technique-disaggregated-inference`, `technique-communication-fallback`