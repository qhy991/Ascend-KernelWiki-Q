---
id: technique-pr-modellink-2134
title: "PR Insight: Ascend/ModelLink #2134"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - attention
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2134"
---

# PR Insight: Ascend/ModelLink #2134

**Title:** bugfix:重构mc代码，修复mc2+matmul_add+swap_attention 报weight没有main_grad属性错误

## Overview
Refactors MC (mixed chunk) code and fixes a bug where the weight parameter lacks the main_grad attribute when using mc2+matmul_add+swap_attention configuration.

## Technical Significance
Bugfix that resolves attribute errors in complex attention scenarios involving MC optimization and swap attention. The refactoring improves code maintainability and fixes gradient computation issues in attention kernels.

## Related
- technique-attention
- technique-operator-fusion