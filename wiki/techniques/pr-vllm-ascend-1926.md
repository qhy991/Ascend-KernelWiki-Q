---
id: technique-pr-vllm-ascend-1926
title: "PR Insight: vllm-project/vllm-ascend #1926"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - allreduce
  - matmul
  - fused-ops
  - tensor-parallel
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1926"
---

# PR Insight: vllm-project/vllm-ascend #1926

**Title:** [Feature]: implement the fusion of allreduce and matmul in prefill phase when tp is enabled

## Overview
This PR implements fusion of allreduce and matmul in the prefill phase when tensor parallelism is enabled. Instead of executing them separately, it uses torch_npu.npu_mm_all_reduce_base to execute both in a fused kernel, achieving 20% performance improvement in eager mode.

## Technical Significance
Communication-computation fusion optimization. Fusing allreduce with matmul reduces synchronization overhead and improves performance by overlapping communication with computation, which is particularly impactful for tensor-parallel prefill operations.

## Related
- `kernel-matmul-ascendc`
- `technique-hccl-optimization`
- `technique-operator-fusion`
- `technique-tensor-parallel`