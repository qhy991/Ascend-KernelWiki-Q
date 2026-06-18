---
id: technique-pr-cann-ops-adv-260
title: "PR Insight: Ascend/cann-ops-adv #260"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - operator-fusion
  - hccl-optimization
  - layernorm
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/260"
---

# PR Insight: Ascend/cann-ops-adv #260

**Title:** 修改MatmulAllReduceAddRmsNorm算子裸指令问题

## Overview
This PR fixes bare instruction issues in the MatmulAllReduceAddRmsNorm operator implementation. The changes address low-level instruction handling problems in the AscendC kernel code, likely related to instruction validation, register allocation, or instruction sequencing in this fused operator.

## Technical Significance
Bare instruction issues in fused operators can lead to correctness bugs, performance degradation, or compilation failures. This fix ensures the MatmulAllReduceAddRmsNorm operator executes correctly by addressing instruction-level problems. The operator combines multiple computation stages (matmul using Cube unit, all-reduce via HCCL, addition, and RMS normalization), making instruction sequencing critical for performance and correctness. The fix likely resolves issues with instruction dependencies, resource conflicts, or instruction validation checks.

## Related
- `technique-operator-fusion`
- `technique-matmul-ascendc`
- `technique-hccl-optimization`
- `technique-instruction-queue`