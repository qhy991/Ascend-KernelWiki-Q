---
id: technique-pr-vllm-ascend-5034
title: "PR Insight: vllm-project/vllm-ascend #5034"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - matmul
  - allreduce
  - rmsnorm
  - graph-pass
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5034"
---

# PR Insight: vllm-project/vllm-ascend #5034

**Title:** [Fusion] [Graph]Add Matmul Allreduce Rmsnorm fusion Pass

## Overview
This PR adds a MatmulAllreduceRmsnorm operator and introduces a graph fusion pass for matmul_allreduce_rmsnorm operations. The implementation includes a pattern matching pass using torch._inductor.pattern_matcher, configuration flags, and patch system integration.

## Technical Significance
Fuses three operations (matrix multiplication, allreduce communication, and RMS normalization) into a single kernel, reducing launch overhead and improving tensor parallelism performance. The fusion pass automatically identifies and combines these patterns in the computation graph.

## Related
- `kernel-matmul-allreduce-rmsnorm`
- `kernel-allreduce`
- `kernel-rmsnorm`
- `technique-operator-fusion`
- `technique-tensor-parallelism`