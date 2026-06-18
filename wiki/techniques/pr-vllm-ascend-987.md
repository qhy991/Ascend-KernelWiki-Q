---
id: technique-pr-vllm-ascend-987
title: "PR Insight: vllm-project/vllm-ascend #987"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - grouped-matmul
  - cumsum
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/987"
---

# PR Insight: vllm-project/vllm-ascend #987

**Title:** [Kernel] Remove cumsum in groupedmatmul

## Overview
This PR removes the cumsum operator from MoE grouped matrix multiplication to improve performance. The optimization requires mc2 operator and graph mode to be effective.

## Technical Significance
Removing unnecessary operators reduces computational overhead in MoE layers. Cumsum can be replaced with more efficient operations in the grouped matmul context, particularly when using mc2 operators in graph mode, leading to better MoE throughput.

## Related
- `kernel-moe`
- `kernel-matmul`
- `technique-graph-mode`