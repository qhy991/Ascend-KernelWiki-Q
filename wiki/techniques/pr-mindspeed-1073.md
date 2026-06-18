---
id: technique-pr-mindspeed-1073
title: "PR Insight: Ascend/MindSpeed #1073"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - adamw
  - optimizer
  - torch
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1073"
---

# PR Insight: Ascend/MindSpeed #1073

**Title:** Adamw新增torch融合优化器选项

## Overview
This PR adds a new fused optimizer option for AdamW using PyTorch's fused implementations. Fused optimizers combine multiple optimization operations into a single kernel for better performance.

## Technical Significance
Fused AdamW optimizers reduce kernel launch overhead and improve memory access patterns on Ascend NPUs. This option provides users with a high-performance optimizer choice that leverages PyTorch's optimizations while maintaining compatibility with MindSpeed's training framework.

## Related
- technique-operator-fusion