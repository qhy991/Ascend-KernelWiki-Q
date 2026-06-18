---
id: technique-pr-mindspeed-2461
title: "PR Insight: Ascend/MindSpeed #2461"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - vpp
  - fb-overlap
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2461"
---

# PR Insight: Ascend/MindSpeed #2461

**Title:** 【master】【bugfix】修复fb-overlap开启vpp 在evaluate报错

## Overview
This PR fixes an error that occurs when fb-overlap (flash-attention overlap) is enabled with VPP (Virtual Pipeline Parallelism) during evaluation. The bug affects the evaluation phase in pipeline parallel training.

## Technical Significance
Resolves compatibility issues between fb-overlap optimization and VPP during inference/evaluation. Flash-attention overlap improves performance by overlapping computation with communication, and ensuring it works correctly in evaluation mode is important for model validation.

## Related
- `kernel-flash-attention`
- `technique-pipeline-scheduling`
- `technique-cube-vector-overlap`