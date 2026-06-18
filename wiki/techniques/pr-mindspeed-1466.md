---
id: technique-pr-mindspeed-1466
title: "PR Insight: Ascend/MindSpeed #1466"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - moe
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1466"
---

# PR Insight: Ascend/MindSpeed #1466

**Title:** 解决Megatron MoE场景开启激活函数重计算报错RANK NaN的问题

## Overview
This PR fixes an issue causing RANK NaN errors when enabling activation function recomputation in Megatron MoE scenarios. The problem likely involves incorrect handling of activation states during recomputation in MoE layers.

## Technical Significance
Resolves numerical stability issues in MoE training with activation recomputation, preventing NaN errors that would otherwise cause training failures. Correct recomputation logic is essential for MoE models to train reliably with memory optimization techniques.

## Related
- `kernel-moe`
- `technique-recomputation`