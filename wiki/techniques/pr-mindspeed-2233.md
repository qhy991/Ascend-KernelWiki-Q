---
id: technique-pr-mindspeed-2233
title: "PR Insight: Ascend/MindSpeed #2233"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - communication
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2233"
---

# PR Insight: Ascend/MindSpeed #2233

**Title:** [feat] moe_overlap with Megatron core_r0.10.0

## Overview
This PR adds MoE (Mixture of Experts) communication overlap optimization to MindSpeed, targeting the Megatron core_r0.10.0 release. The feature overlaps MoE communication (all-to-all and all-gather) with computation to hide communication latency.

## Technical Significance
MoE communication overlap is a critical optimization for Mixture of Experts models on Ascend NPUs. By overlapping communication with computation, this feature reduces the impact of HCCL communication latency on training throughput. The optimization supports both all-to-all and all-gather communication patterns, which are the dominant communication operations in MoE routing and expert dispatch. This feature is essential for efficient training of large-scale MoE models on Ascend hardware, enabling near-linear scaling with expert parallelism.

## Related
- `technique-hccl-optimization`
- `technique-cube-vector-overlap`