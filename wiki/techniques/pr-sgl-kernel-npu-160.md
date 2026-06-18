---
id: technique-pr-sgl-kernel-npu-160
title: "PR Insight: sgl-project/sgl-kernel-npu #160"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - topk
  - dispatch
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/160"
---

# PR Insight: sgl-project/sgl-kernel-npu #160

**Title:** support shallow fused topk=-1

## Overview
Adds support for shallow fused topk=-1 in the DeepEP dispatch operators. This modification enables the fused DeepMoE operator to handle scenarios where topk is set to -1, which typically indicates using all experts or a dynamic topk selection mechanism.

## Technical Significance
This feature is crucial for MoE inference flexibility, allowing dynamic expert selection without requiring a fixed topk value. The implementation in `cam_moe_distribute_dispatch` operator supports variable expert selection patterns, which is important for adaptive MoE routing and load balancing strategies in DeepEP inference pipelines.

## Related
- `wiki-kernel-moe`
- `wiki-technique-operator-fusion`
- `wiki-technique-moe`