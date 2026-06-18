---
id: technique-pr-mindspeed-1151
title: "PR Insight: Ascend/MindSpeed #1151"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - torch
  - documentation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1151"
---

# PR Insight: Ascend/MindSpeed #1151

**Title:** MOE迭代torch接口文档输出字段描述完善

## Overview
This PR improves documentation for MoE (Mixture of Experts) iteration Torch interface output field descriptions. The documentation updates clarify the meaning and structure of fields returned by MoE operations.

## Technical Significance
Clear interface documentation is essential for users integrating MindSpeed's MoE features with PyTorch workflows. These improvements help users understand MoE operation outputs correctly, enabling proper integration and debugging of MoE models on Ascend hardware.

## Related
- kernel-moe