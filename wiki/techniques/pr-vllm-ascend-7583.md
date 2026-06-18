---
id: technique-pr-vllm-ascend-7583
title: "PR Insight: vllm-project/vllm-ascend #7583"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-v2
  - combine-v2
  - hierarchical-communication
  - mc2
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7583"
---

# PR Insight: vllm-project/vllm-ascend #7583

**Title:** [feat] support dispatch_v2/combine_v2 hierarchy communication

## Overview
This PR adds support for hierarchical communication for dispatch_v2 and combine_v2 MoE operations. It introduces enable_mc2_hierarchy_comm configuration that sets comm_alg to "hierarchy" for MC2 operations between two super pods, with validation for compatible PTA/CANN versions and conflicts with fused_mc2 op.

## Technical Significance
This feature matters for large-scale MoE inference on Ascend. Hierarchical communication optimizes MC2 operations across super pods, reducing cross-pod communication overhead. This enables efficient scaling of MoE models across multiple compute clusters, improving throughput for distributed MoE deployments.

## Related
- technique-moe
- technique-hierarchical-communication
- technique-mc2