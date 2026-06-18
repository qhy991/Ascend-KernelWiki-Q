---
id: technique-pr-mindspeed-2205
title: "PR Insight: Ascend/MindSpeed #2205"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - optimizer
  - adamw
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2205"
---

# PR Insight: Ascend/MindSpeed #2205

**Title:** 接口替换：将torch_npu.npu_apply_adam_w替换为torch._fused_adamw

## Overview
This PR replaces the torch_npu.npu_apply_adam_w interface with torch._fused_adamw in MindSpeed. The change migrates to the standard PyTorch fused AdamW operator for optimizer step computation.

## Technical Significance
Migrating to torch._fused_adamw standardizes the optimizer interface and ensures compatibility with standard PyTorch APIs. The fused AdamW operator performs weight updates, gradient clipping, and learning rate scheduling in a single kernel launch, reducing kernel launch overhead and improving memory bandwidth utilization on Ascend NPUs. This optimization is particularly beneficial for distributed training where optimizer steps are frequent and communication overhead is significant.

## Related
- `technique-operator-fusion`
- `technique-nz-tiling`