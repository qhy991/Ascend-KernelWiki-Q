---
id: technique-pr-modellink-2318
title: "PR Insight: Ascend/ModelLink #2318"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - bugfix
  - router
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2318"
---

# PR Insight: Ascend/ModelLink #2318

**Title:** [bugfix] moe_tp_extend_ep in router

## Overview
Fixes a bug in the router logic for MoE tensor parallelism with expert parallelism extension. The bug was affecting how tokens are routed to experts in distributed MoE training scenarios.

## Technical Significance
Critical bugfix for MoE training correctness. The router is the core component that determines which experts process which tokens, and any errors here directly impact model accuracy and training stability across distributed NPU setups.

## Related
- technique-moe
- technique-hccl-optimization