---
id: technique-pr-vllm-ascend-2839
title: "PR Insight: vllm-project/vllm-ascend #2839"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2839"
---

# PR Insight: vllm-project/vllm-ascend #2839

**Title:** [v0.9.1]fix bug of eplb

## Overview
This PR fixes a bug in the EPLB (Expert Parallel Load Balancing) implementation in the vllm_ascend/eplb/utils.py module.

## Technical Significance
Bug fix for Expert Parallel Load Balancing, which is critical for balancing workload across experts in MoE models. Proper load balancing ensures efficient resource utilization and prevents expert overload, which is essential for MoE model performance and stability on Ascend NPUs.

## Related
- `kernel-moe-ascendc`, `technique-moe-optimization`, `technique-load-balancing`