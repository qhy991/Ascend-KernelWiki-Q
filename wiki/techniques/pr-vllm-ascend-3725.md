---
id: technique-pr-vllm-ascend-3725
title: "PR Insight: vllm-project/vllm-ascend #3725"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - reduce-scatter
  - operator-fusion
  - w8a8
  - performance
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3725"
---

# PR Insight: vllm-project/vllm-ascend #3725

**Title:** [0.11.0][Perf] Add fused matmul/reduce-scatter kernel for performance optimization.

## Overview
This is a cherry-pick of PR #3693 to the v0.11.0 branch, introducing a fused kernel for matrix multiplication and reduce-scatter operations. The fused kernel supports both unquantized (BFloat16) and W8A8 quantized models, implemented in `vllm_ascend/ops/linear_op.py` with 82 lines added and 7 lines removed.

## Technical Significance
Backporting performance optimizations to release branches ensures users benefit from improved throughput. Fusing matmul with reduce-scatter reduces memory traffic and kernel launch overhead, particularly valuable for tensor parallel workloads. Supporting both quantized and unquantized data types ensures broad applicability across model types.

## Related
- `technique-matmul`
- `technique-reduce-scatter`
- `technique-operator-fusion`