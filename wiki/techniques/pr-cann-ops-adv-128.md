---
id: technique-pr-cann-ops-adv-128
title: "PR Insight: cann-ops-adv #128"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - ascendc
  - mte
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/128"
---

# PR Insight: cann-ops-adv #128 - 新增 MoeTokenPermute算子

## Overview
This PR adds the MoeTokenPermute operator, which reorders (permutes) tokens based on their assigned experts, grouping tokens by expert for efficient batched expert computation in MoE models.

## Technical Significance
Token permutation is essential for MoE efficiency. After routing, tokens assigned to the same expert must be grouped together in memory to enable efficient batched GEMM via GroupedMatmul. MoeTokenPermute handles this memory reordering on Ascend NPUs with optimized data movement patterns.

## Related
- `kernel-moe`
- `technique-data-reuse`
- `hw-mte`
- `hw-unified-buffer`