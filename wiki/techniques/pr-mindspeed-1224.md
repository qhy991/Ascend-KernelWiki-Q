---
id: technique-pr-mindspeed-1224
title: "PR Insight: Ascend/MindSpeed #1224"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - coc
  - matmul
  - fusion
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1224"
---

# PR Insight: Ascend/MindSpeed #1224

**Title:** COC+matmul_add融合优化算子适配

## Overview
This PR adapts the COC (likely communication or computation optimization) with matmul_add fused optimization operators. This involves integrating a custom fused operator that combines matrix multiplication with addition for the COC optimization path.

## Technical Significance
Fused matmul_add operators reduce memory bandwidth usage and improve performance by combining operations in a single kernel pass on Ascend hardware. This adaptation for COC optimizations ensures that communication/computation overlap benefits work correctly with these efficient fused implementations.

## Related
- technique-operator-fusion
- kernel-matmul
- kernel-elementwise