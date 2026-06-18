---
id: technique-pr-vllm-ascend-3837
title: "PR Insight: vllm-project/vllm-ascend #3837"
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
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3837"
---

# PR Insight: vllm-project/vllm-ascend #3837

**Title:** [v0.11.0][Bugfix]Avoid using the fusion operator in the MOE model

## Overview
This is a cherry-pick of PR #3834 to the v0.11.0 branch, adding shape-based conditionals to avoid using the MatmulReduceScatter fusion operator in small-shape scenarios. The adaptive selection prevents performance degradation when fusion overhead exceeds benefits.

## Technical Significance
Backporting adaptive operator selection ensures v0.11.0 users get optimal performance across different tensor sizes, particularly for MoE workloads with variable operator dimensions.

## Related
- `technique-operator-fusion`
- `technique-matmul`
- `technique-moe`