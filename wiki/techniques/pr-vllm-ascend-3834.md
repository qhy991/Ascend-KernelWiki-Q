---
id: technique-pr-vllm-ascend-3834
title: "PR Insight: vllm-project/vllm-ascend #3834"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul-reduce-scatter
  - operator-fusion
  - moe
  - performance
  - shape-based-selection
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3834"
---

# PR Insight: vllm-project/vllm-ascend #3834

**Title:** [Main][Bugfix]Avoid using the fusion operator in the MOE model

## Overview
This PR adds shape-based conditionals to avoid using the MatmulReduceScatter fusion operator in small-shape scenarios where it causes performance degradation. The implementation adds logic to `vllm_ascend/ops/linear_op.py` and `vllm_ascend/ascend_forward_context.py` to select between fused and unfused operators based on tensor dimensions.

## Technical Significance
Fused operators improve performance for large tensors but can have overhead for small tensors due to kernel launch and synchronization costs. This adaptive selection ensures optimal performance across different tensor sizes, particularly important for MoE models where operator sizes vary significantly.

## Related
- `technique-operator-fusion`
- `technique-matmul`
- `technique-moe`