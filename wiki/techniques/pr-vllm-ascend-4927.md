---
id: technique-pr-vllm-ascend-4927
title: "PR Insight: vllm-project/vllm-ascend #4927"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - torchair
  - cleanup
  - state-management
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4927"
---

# PR Insight: vllm-project/vllm-ascend #4927

**Title:** [MoE][TorchAir] Remove FusedMoEState

## Overview
This PR removes FusedMoEState which was previously used by torchair. The change is made to vllm_ascend/ascend_forward_context.py.

## Technical Significance
Cleans up torchair-specific state management code, simplifying the MoE implementation. The removal indicates that FusedMoEState is no longer needed for current MoE operations.

## Related
- `kernel-fused-moe`
- `technique-moe-state`