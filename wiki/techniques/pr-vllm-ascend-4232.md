---
id: technique-pr-vllm-ascend-4232
title: "PR Insight: vllm-project/vllm-ascend #4232"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - moe
  - redundant-experts
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4232"
---

# PR Insight: vllm-project/vllm-ascend #4232

**Title:** 【EPLB】Eplb Redundant Experts Bugfix

## Overview
This PR fixes the redundant experts calculation logic in EPLB. The fix allows correct calculation of redundant experts using the experts_map, eliminating the need for users to configure init_redundancy_expert parameter when passing the map. The accuracy of EPLB was tested with and without redundant experts.

## Technical Significance
Proper redundant experts calculation is essential for EPLB accuracy and load balancing. The bug fix ensures correct expert routing and load distribution. Removing the need for manual redundant expert configuration simplifies user experience while maintaining correctness.

## Related
- `technique-eplb`, `technique-moe`, `technique-redundant-experts`, `pattern-load-balancing`, `pattern-configuration-simplification`