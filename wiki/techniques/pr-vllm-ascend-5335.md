---
id: technique-pr-vllm-ascend-5335
title: "PR Insight: vllm-project/vllm-ascend #5335"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - matmul
  - all-reduce
  - layernorm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5335"
---

# PR Insight: vllm-project/vllm-ascend #5335

**Title:** [kernel] fix matmul_allreduce_add_rmsnorm_kernel

## Overview
This PR fixes the matmul_allreduce_add_rmsnorm kernel by adding HCCL initialization and SetCcTiling interface calls. The fix ensures proper communication setup for multi-card scenarios.

## Technical Significance
The matmul_allreduce_add_rmsnorm fused kernel is performance-critical for transformer layers. Proper HCCL initialization is essential for correct all-reduce operations across multiple Ascend NPUs in distributed inference scenarios.

## Related
- technique-operator-fusion
- technique-hccl-optimization
- technique-layernorm