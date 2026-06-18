---
id: technique-pr-vllm-ascend-3693
title: "PR Insight: vllm-project/vllm-ascend #3693"
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
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3693"
---

# PR Insight: vllm-project/vllm-ascend #3693

**Title:** [Main][Perf] Add fused matmul/reduce-scatter kernel for performance optimization.

## Overview
This PR introduces a fused kernel combining matrix multiplication and reduce-scatter operations for performance optimization. The fused kernel supports both unquantized (BFloat16) and W8A8 quantized models. The implementation adds 82 lines to `vllm_ascend/ops/linear_op.py` and removes 7 lines of previous implementation.

## Technical Significance
Fusing matmul with reduce-scatter eliminates intermediate memory writes/reads and reduces kernel launch overhead. This is particularly valuable for distributed training/inference where reduce-scatter follows matmul operations. Supporting both quantized and unquantized data types ensures broad applicability across model types, improving throughput for tensor parallel workloads.

## Related
- `technique-matmul`
- `technique-reduce-scatter`
- `technique-operator-fusion`