---
id: technique-pr-vllm-ascend-4150
title: "PR Insight: vllm-project/vllm-ascend #4150"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - moe
  - bugfix
  - log2phy
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4150"
---

# PR Insight: vllm-project/vllm-ascend #4150

**Title:** [0.11.0-dev][Bugfix][EPLB] Quick fix for missing log2phy conversion

## Overview
This PR is a quick fix for missing log2phy (logical to physical) conversion in MC2 token_dispatcher for EPLB (Expert Parallel Load Balancing). The fix adds the missing conversion that was already fixed in the main branch, ensuring correct block table handling in EPLB scenarios.

## Technical Significance
Log2phy conversion is essential for correctly mapping logical block indices to physical memory locations. Missing this conversion causes incorrect memory access in EPLB scenarios, leading to wrong results or crashes. The fix ensures EPLB works correctly on the v0.11.0-dev branch.

## Related
- `technique-eplb`, `technique-moe`, `pattern-memory-mapping`, `technique-block-management`