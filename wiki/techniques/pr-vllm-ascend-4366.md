---
id: technique-pr-vllm-ascend-4366
title: "PR Insight: vllm-project/vllm-ascend #4366"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4366"
---

# PR Insight: vllm-project/vllm-ascend #4366

**Title:** [Bugfix][MoE] enable force_load_balance in aclgraph

**Author:** Pr0Wh1teGivee | **Merged:** 2025-11-24

## Overview
Fixes a bug in fused_moe operations. The issue affects model accuracy and stability. Changes are focused on core operator implementations.

## Technical Significance
MoE operations benefit from improved load balancing and expert routing efficiency. Changes affect how expert weights are loaded and distributed, reducing communication overhead and improving parallelism. These optimizations are crucial for scaling MoE models on Ascend NPU clusters.

## Related
- `kernel-moe-ascendc`
