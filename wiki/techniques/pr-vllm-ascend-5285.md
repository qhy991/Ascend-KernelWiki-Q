---
id: technique-pr-vllm-ascend-5285
title: "PR Insight: vllm-project/vllm-ascend #5285"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - eplb
  - expert-mapping
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5285"
---

# PR Insight: vllm-project/vllm-ascend #5285

**Title:** Bugfix: Align expert map shapes with redundant experts in EPLB adjustment

## Overview
This PR fixes a shape mismatch bug between `expert_placement_map` and `log2phy_expert_map` when redundant experts are enabled. The fix unifies expert map shape calculation logic to align with the total number of experts (including redundant experts) and adds consistency checks.

## Technical Significance
Proper expert map alignment is critical for correct MoE routing when using redundant experts with EPLB (Expert Load Balancer). The fix prevents tensor shape errors and ensures accurate expert routing in distributed MoE deployments on Ascend NPUs.

## Related
- technique-moe
- technique-expert-parallelism
- technique-load-balancing