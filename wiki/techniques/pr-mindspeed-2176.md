---
id: technique-pr-mindspeed-2176
title: "PR Insight: Ascend/MindSpeed #2176"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - tensor-parallel
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2176"
---

# PR Insight: Ascend/MindSpeed #2176

**Title:** fix bug of tp_extend_ep

## Overview
This PR fixes a bug in the tp_extend_ep (tensor parallel extend expert parallel) feature. The feature combines tensor parallelism with expert parallelism for MoE (Mixture of Experts) models.

## Technical Significance
The tp_extend_ep feature is critical for scaling MoE models on Ascend NPUs, allowing experts to be distributed across both tensor parallel and expert parallel dimensions. The bug fix addresses issues in the combined parallel strategy, ensuring correct tensor partitioning and communication patterns. This optimization is essential for efficient MoE training, as it reduces communication overhead and improves load balancing across experts. The fix likely addresses edge cases in tensor shape handling or HCCL communication for hybrid parallel configurations.

## Related
- `technique-hccl-optimization`
- `technique-cube-vector-overlap`