---
id: technique-pr-vllm-ascend-4919
title: "PR Insight: vllm-project/vllm-ascend #4919"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - dynamic-load-balance
  - fused-alltoall
  - all-to-all
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4919"
---

# PR Insight: vllm-project/vllm-ascend #4919

**Title:** [Bugfix] dynamic eplb does't use fused_alltoall

## Overview
This PR fixes an issue where the fused alltoall operator doesn't handle tensor lists, which are used by dynamic load balancing weights. The fix disables the fused alltoall operator when using dynamic EPLB (expert load balancing).

## Technical Significance
Ensures correct MoE expert load balancing in dynamic scenarios by falling back to a non-fused alltoall implementation when weights are in list format. Prevents errors in distributed expert weight distribution.

## Related
- `technique-eplb`
- `kernel-fused-alltoall`
- `technique-dynamic-load-balancing`
- `kernel-moe`