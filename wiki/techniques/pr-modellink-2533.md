---
id: technique-pr-modellink-2533
title: "PR Insight: Ascend/ModelLink #2533"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - optimization
  - operator-fusion
  - scatter-add
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2533"
---

# PR Insight: Ascend/ModelLink #2533

**Title:** 冗余mask消除&amp;scatter_add算子消除替换

## Overview
This PR eliminates redundant mask operations and replaces/eliminates scatter_add operators. These optimizations reduce unnecessary computation and improve training efficiency on Ascend hardware.

## Technical Significance
Eliminating redundant masks reduces computation overhead in attention and masking operations. Replacing scatter_add with more efficient operators improves performance for gradient accumulation and MoE routing operations.

## Related
- operator optimization
- mask elimination
- scatter operations