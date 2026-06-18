---
id: technique-pr-mindspeed-1798
title: "PR Insight: Ascend/MindSpeed #1798"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - all-to-all
  - shared-expert
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1798"
---

# PR Insight: Ascend/MindSpeed #1798

**Title:** moe-all2all-overlap支持shared_expert_gate

## Overview
This PR adds support for shared_expert_gate in MoE all-to-all overlap optimization. The feature enables shared expert gating with overlapped communication and computation in MoE architectures.

## Technical Significance
Shared expert gates are important for MoE efficiency, allowing certain experts to be shared across tasks. Supporting this with all-to-all overlap improves communication efficiency and reduces latency for MoE workloads on Ascend NPUs.

## Related
- moe-routing techniques
- all-to-all communication
- technique-hccl-optimization