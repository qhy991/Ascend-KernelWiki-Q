---
id: technique-pr-vllm-ascend-121
title: "PR Insight: vllm-project/vllm-ascend #121"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - distributed
  - hccs-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/121"
---

# PR Insight: vllm-project/vllm-ascend #121

**Title:** [Feature] Implement EP-compatible fused_moe

## Overview
This PR enables Expert-Parallel (EP) for Ascend devices in the fused_moe operator. The implementation adds 270 lines and modifies 129 lines in fused_moe.py, plus comprehensive test coverage. Users can enable EP via enable_expert_parallel=True.

## Technical Significance
EP distributes experts across devices, reducing memory per device for large MoE models. This Ascend-specific EP-compatible MoE implementation allows scaling MoE workloads across multiple NPUs, essential for DeepSeek and other large expert models.

## Related
- kernel-moe
- technique-hccs-optimization
- technique-moe