---
id: technique-pr-modellink-2502
title: "PR Insight: Ascend/ModelLink #2502"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - weight-conversion
  - tensor-parallel
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2502"
---

# PR Insight: Ascend/ModelLink #2502

**Title:** [bugfix]权重转换tp-extend-ep&mlp部分layer idx计算

## Overview
This PR fixes weight conversion issues related to tensor parallelism extension, expert parallelism, and MLP layer index calculations. Weight conversion handles model transformations for different parallelism strategies.

## Technical Significance
Fixing weight conversion ensures correct model distribution across TP/EP configurations on Ascend hardware. Proper layer index calculation is critical for MLP and MoE layer mapping in parallel training.

## Related
- weight conversion
- tensor parallelism
- expert parallelism