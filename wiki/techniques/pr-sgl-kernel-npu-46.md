---
id: technique-pr-sgl-kernel-npu-46
title: "PR Insight: sgl-project/sgl-kernel-npu #46"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cache-assign
  - operator-fusion
  - ascendc
  - optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/46"
---

# PR Insight: sgl-project/sgl-kernel-npu #46

**Title:** support fused cache assign op

## Overview
This PR fuses the entire cache assign operation into a single optimized kernel, replacing the previous multi-stage implementation. Consolidates cache_loc_assign logic (194 lines new kernel), removes int32 variant, and updates tests.

## Technical Significance
Achieves performance improvement through operator fusion, eliminating intermediate memory transfers between cache assignment stages. Fusion reduces kernel launch overhead and improves memory locality, critical for cache-intensive inference operations like KV cache management.

## Related
- technique-operator-fusion
- technique-cache-optimization
- technique-kv-cache