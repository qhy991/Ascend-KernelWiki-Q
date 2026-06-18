---
id: technique-pr-vllm-ascend-4606
title: "PR Insight: vllm-project/vllm-ascend #4606"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4606"
---

# PR Insight: vllm-project/vllm-ascend #4606

**Title:** [Kernel] add custom op MatmulAllreduceAddRmsnorm

**Author:** Trunrain | **Merged:** 2025-12-10

## Overview
Adds new functionality for test_matmul_allreduce_add_rmsnorm, matmul_allreduce_add_rmsnorm_utils, matmul_allreduce_add_rmsnorm_ operations. The feature enhances model capabilities and performance.

## Technical Significance
This change improves the robustness and performance of core inference operations. Better handling of edge cases and more efficient operator implementations contribute to overall system stability and throughput.

## Related
- `kernel-matmul-ascendc`
