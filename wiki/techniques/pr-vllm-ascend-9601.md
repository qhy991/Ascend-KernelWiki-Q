---
id: technique-pr-vllm-ascend-9601
title: "PR Insight: vllm-project/vllm-ascend #9601"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gdn
  - fused-gdn-gating
  - ascendc
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9601"
---

# PR Insight: vllm-project/vllm-ascend #9601

**Title:** [Ops][Feature] Add fused_gdn_gating AscendC custom operator

## Overview
This PR adds a fused_gdn_gating AscendC custom operator that combines GDN gating operations into a single optimized kernel. The implementation includes complete operator definitions, tiling logic, kernel implementation, ACLNN integration, torch bindings, and E2E tests.

## Technical Significance
Fusing GDN gating operations reduces kernel launch overhead and enables more efficient memory access patterns by keeping intermediate results in fast memory. This optimization significantly improves performance for models using GDN operations, which are important for certain sequence modeling and time-series tasks.

## Related
- `technique-operator-fusion`
- `hw-cube-unit`
- `hw-vector-unit`