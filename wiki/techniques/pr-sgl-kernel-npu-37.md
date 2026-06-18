---
id: technique-pr-sgl-kernel-npu-37
title: "PR Insight: sgl-project/sgl-kernel-npu #37"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - notify-dispatch
  - prefill
  - event-sync
  - ascendc
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/37"
---

# PR Insight: sgl-project/sgl-kernel-npu #37

**Title:** add notify dispatch kernel for prefill stage

## Overview
This PR adds a notify dispatch kernel for the prefill stage, implementing synchronization mechanisms for dispatch operations. Includes tiling logic (267 lines), kernel implementation (456 lines), sync_collectives (426 lines), and ACLNN API integration.

## Technical Significance
Enables proper synchronization of dispatch operations in Deep EP prefill stage, preventing race conditions and ensuring correct expert execution order. The notify mechanism coordinates distributed dispatch across multiple ranks or devices, essential for MoE inference correctness.

## Related
- technique-event-sync
- technique-dispatch-synchronization
- technique-collective-communication
- technique-ascendc