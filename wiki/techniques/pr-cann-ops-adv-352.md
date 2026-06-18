---
id: technique-pr-cann-ops-adv-352
title: "PR Insight: Ascend/cann-ops-adv #352"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fag
  - attention
  - transformer
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/352"
---

# PR Insight: Ascend/cann-ops-adv #352

**Title:** add fag

## Overview
This PR adds FAG (Flash Attention Group) operator support to the CANN ops library. FAG implements grouped attention computations, optimizing multiple attention heads or batches together for improved hardware utilization on Ascend.

## Technical Significance
The FAG operator is a significant addition for transformer model performance. By grouping attention computations, it can better utilize Ascend's Cube units and reduce kernel launch overhead. Grouped attention is particularly beneficial for batched inference and training where multiple attention operations can be processed simultaneously. This operator likely includes optimizations for memory layout, tiling strategies, and mask handling specific to Ascend's architecture.

## Related
- `technique-flash-attention`
- `technique-attention-optimization`
- `technique-operator-grouping`
- `technique-cube-unit`