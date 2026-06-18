---
id: technique-pr-sgl-kernel-npu-313
title: "PR Insight: sgl-project/sgl-kernel-npu #313"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - moe
  - double-buffering
  - topk
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/313"
---

# PR Insight: sgl-project/sgl-kernel-npu #313

**Title:** support the situation that topk maybe -1 on machine A3

## Overview
This PR enables DeepEP MoE operators to handle the special case where topk=-1 on Ascend A3 machines. The changes modify dispatch and combine kernel tiling logic to properly handle the -1 topk scenario, which indicates all experts should be selected. The implementation updates multiple kernel files including cam_moe_combine_normal, cam_moe_dispatch_normal, and dispatch_layout across both ops and ops2 directories.

## Technical Significance
This fix enables dynamic expert selection on A3 hardware where topk=-1 is a valid configuration mode. The modification ensures proper memory allocation and tiling parameter calculation when all experts need to be routed through the MoE layers, which is critical for models requiring full expert evaluation during certain inference phases.

## Related
- `kernel-moe-dispatch`, `kernel-moe-combine`, `technique-operator-fusion`, `hw-hccs`