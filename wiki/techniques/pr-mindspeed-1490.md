---
id: technique-pr-mindspeed-1490
title: "PR Insight: Ascend/MindSpeed #1490"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - ripipe
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1490"
---

# PR Insight: Ascend/MindSpeed #1490

**Title:** ripipe切换重计算实现方式为torch.autograd.function，兼容megatron moe

## Overview
This PR changes the ripipe (likely a pipeline parallelism implementation) recomputation implementation to use torch.autograd.function for better compatibility with Megatron MoE. The change improves integration with PyTorch's autograd system.

## Technical Significance
Enhances compatibility with Megatron MoE by using standard PyTorch autograd mechanisms for recomputation. This approach improves integration and reduces custom code maintenance while maintaining correct gradient computation.

## Related
- `technique-recomputation`
- `kernel-moe`