---
id: technique-pr-vllm-ascend-6537
title: "PR Insight: vllm-project/vllm-ascend #6537"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - kernel-optimization
  - adaptive-tiling
  - triton
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6537"
---

# PR Insight: vllm-project/vllm-ascend #6537

**Title:** perf: adaptive block size selection in linear_persistent kernel

## Overview
This PR optimizes the linear_persistent kernel by replacing fixed 128x128x128 block sizes with adaptive selection logic that considers matrix dimensions (M, N, K), device NPU vector core count, and data type. The optimization uses size-proportional allocation for small matrices, balanced distribution for medium matrices, and dominant dimension optimization for large matrices.

## Technical Significance
Improves hardware utilization and throughput for batch-invariant linear operations in LLM inference by adapting kernel tiling to workload characteristics. The adaptive sizing maximizes NPU vector core occupancy and memory efficiency across diverse matrix shapes and batch sizes.

## Related
- `kernel-matmul-ascendc`