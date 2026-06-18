---
id: technique-pr-vllm-ascend-5119
title: "PR Insight: vllm-project/vllm-ascend #5119"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - matmul
  - aclnn
  - layernorm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5119"
---

# PR Insight: vllm-project/vllm-ascend #5119

**Title:** restore matmul_allreduce_add_rmsnrom aclnn interface

## Overview
This PR restores the ACLNN interface for the matmul_allreduce_add_rmsnorm fused operator kernel, reverting a previous change. The restoration ensures proper kernel registration and execution on Ascend NPUs.

## Technical Significance
The matmul_allreduce_add_rmsnorm operator is a performance-critical fused kernel that combines matrix multiplication, all-reduce communication, and RMS normalization. Proper ACLNN interface linkage is essential for this operator to work correctly on Ascend NPUs.

## Related
- technique-operator-fusion
- technique-hccl-optimization
- technique-layernorm