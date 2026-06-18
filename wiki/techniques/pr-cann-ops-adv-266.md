---
id: technique-pr-cann-ops-adv-266
title: "PR Insight: Ascend/cann-ops-adv #266"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - elementwise
  - data-reuse
  - transformer
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/266"
---

# PR Insight: Ascend/cann-ops-adv #266

**Title:** unpermute、permuteGrad开源整改

## Overview
This PR refactors and open-sources improvements to the unpermute and permute gradient operators. The changes modernize the implementation, address open-source compliance requirements, and potentially optimize the tensor permutation operations used in MoE and other transformer models.

## Technical Significance
Permutation and unpermutation operators are essential for MoE models where tokens are reordered according to expert assignment. Efficient implementation of these operations is critical for minimizing overhead in the MoE forward and backward passes. This refactoring likely improves code maintainability, addresses open-source licensing or attribution issues, and may include performance optimizations for tensor reordering patterns. The gradient operator ensures proper backpropagation through permutation operations, which is crucial for training sparse MoE architectures.

## Related
- `technique-moe-ascendc`
- `technique-data-reuse`
- `technique-elementwise-operations`
- `technique-tensor-operations`