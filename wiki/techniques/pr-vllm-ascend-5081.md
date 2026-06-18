---
id: technique-pr-vllm-ascend-5081
title: "PR Insight: vllm-project/vllm-ascend #5081"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - attention
  - refactoring
  - sliding-window
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5081"
---

# PR Insight: vllm-project/vllm-ascend #5081

**Title:** [Refactor] 4/N Distinguish the branches based on the applicable scenarios of PA and FIA Ops.

## Overview
This PR refactors the attention implementation to clearly distinguish branches based on applicable scenarios for PagedAttention (PA) and FusedInferAttention (FIA) operators. The refactoring makes code logic clearer and prepares for future features like sliding windows and sink tokens, and enables removal of PA ops once FIA is fully ready.

## Technical Significance
This architectural refactoring simplifies the attention operator selection logic, reducing conditional complexity and enabling cleaner code paths for different attention scenarios. It also prepares the codebase for future optimizations and feature additions on Ascend NPUs.

## Related
- technique-attention
- technique-flash-attention
- technique-sliding-window