---
id: technique-pr-sgl-kernel-npu-141
title: "PR Insight: sgl-project/sgl-kernel-npu #141"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - topk
  - hccs
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/141"
---

# PR Insight: sgl-project/sgl-kernel-npu #141

**Title:** Supports running the Longcat model with topk=-1 on A2 CANN 8.3

## Overview
This PR enables the Longcat model to run with topk=-1 on Ascend A2 with CANN 8.3. Changes include reverting padding generation from randperm to arange and using "fullmesh" as the commAlg parameter for dispatch/combine operators.

## Technical Significance
Longcat with topk=-1 requires all experts to participate, creating different communication patterns than sparse routing. The fullmesh algorithm and deterministic padding ensure predictable communication performance. CANN 8.3 compatibility ensures the operator works with the latest Ascend software stack.

## Related
- `technique-moe`, `technique-hccl-optimization`, `hw-hccs`