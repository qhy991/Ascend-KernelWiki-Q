---
id: technique-pr-modellink-2328
title: "PR Insight: Ascend/ModelLink #2328"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - weight-conversion
  - tensor-parallelism
  - expert-parallelism
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2328"
---

# PR Insight: Ascend/ModelLink #2328

**Title:** 权重转换tp_extend_ep逻辑修正

## Overview
Fixes the logic for weight conversion when using tensor parallelism with expert parallelism extension. The correction ensures proper weight distribution across both TP and EP dimensions during model weight transformation.

## Technical Significance
Critical fix for MoE training scenarios that combine tensor parallelism and expert parallelism. The weight conversion logic directly impacts how expert weights are sharded and synchronized across devices, which is essential for correct MoE model training and inference in modellink.

## Related
- technique-moe
- technique-hccl-optimization
- technique-data-reuse