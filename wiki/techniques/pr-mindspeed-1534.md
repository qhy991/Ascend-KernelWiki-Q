---
id: technique-pr-mindspeed-1534
title: "PR Insight: Ascend/MindSpeed #1534"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - coc
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1534"
---

# PR Insight: Ascend/MindSpeed #1534

**Title:** COC打开matmul_add，main_grad缺失修复

## Overview
This PR fixes an issue where main_grad was missing when COC (likely a compilation or optimization flag) enabled matmul_add operations. The fix ensures gradient information is properly preserved when using fused matmul-add.

## Technical Significance
Resolves gradient computation issues when using optimized matmul-add fusion, preventing incorrect training or gradient accumulation problems. Proper gradient handling is essential for correct model training.

## Related
- `kernel-matmul`
- `technique-operator-fusion`