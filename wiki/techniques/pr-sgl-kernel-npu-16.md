---
id: technique-pr-sgl-kernel-npu-16
title: "PR Insight: sgl-project/sgl-kernel-npu #16"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - moe
  - shared-expert
  - configuration
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/16"
---

# PR Insight: sgl-project/sgl-kernel-npu #16

**Title:** support shared expert

## Overview
This PR adds support for configuring shared expert ranks in Deep EP through the MOE_SHARED_EXPERT_RANK_NUM environment variable (default 0). Modifies config.cpp/hpp and deep_ep.cpp/hpp to handle shared expert allocation.

## Technical Significance
Enables flexible MoE (Mixture of Experts) architecture configurations by allowing shared experts across ranks. Shared experts improve compute efficiency by reusing expert computations, particularly valuable for models with common expert patterns. The environment variable interface provides runtime configurability without code changes.

## Related
- technique-moe
- technique-shared-expert
- technique-moe-routing