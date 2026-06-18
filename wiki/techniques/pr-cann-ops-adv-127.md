---
id: technique-pr-cann-ops-adv-127
title: "PR Insight: cann-ops-adv #127"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - grouped-gemm
  - matmul
  - ascendc
  - moe
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/127"
---

# PR Insight: cann-ops-adv #127 - 新增GroupedMatmul算子

## Overview
This PR adds the GroupedMatmul operator, which performs multiple matrix multiplications with different matrices in a single kernel launch, commonly used in MoE expert computation.

## Technical Significance
GroupedMatmul eliminates the overhead of launching multiple GEMM kernels, which is critical for MoE models that need to compute many expert outputs simultaneously. By batching expert GEMMs, this operator significantly improves MoE inference throughput on Ascend NPUs.

## Related
- `kernel-grouped-gemm`
- `kernel-matmul`
- `kernel-moe`
- `hw-cube-unit`