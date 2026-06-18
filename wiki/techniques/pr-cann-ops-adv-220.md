---
id: technique-pr-cann-ops-adv-220
title: "PR Insight: cann-ops-adv #220"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - communication
  - tensor-parallel
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/220"
---

# PR Insight: cann-ops-adv #220 - matmulReduceScatter编译工程修复

## Overview
This PR fixes compilation issues in the build configuration for the matmulReduceScatter operator, enabling correct compilation of the fused matmul-ReduceScatter operation.

## Technical Significance
Compilation fixes are essential for operator usability. This fix ensures developers can build and deploy the matmulReduceScatter operator, which is critical for efficient tensor parallel inference on Ascend NPUs.

## Related
- `kernel-matmul`
- `technique-tensor-parallel-overlap`
- `technique-hccl-optimization`
- `hw-hccs`