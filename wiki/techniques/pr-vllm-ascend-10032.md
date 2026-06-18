---
id: technique-pr-vllm-ascend-10032
title: "PR Insight: vllm-project/vllm-ascend #10032"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - async-token-correction
  - decode-state
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10032"
---

# PR Insight: vllm-project/vllm-ascend #10032

**Title:** [BugFix][CP] Rebuild stale decode state after async token correction

## Overview
This PR fixes context parallel issues where decode state becomes stale after async token correction. It ensures that decode state is properly rebuilt to reflect token corrections, maintaining consistency in CP scenarios.

## Technical Significance
Fixes decode state consistency in context parallel scenarios with async token correction. Ensures that all CP ranks have consistent decode state after token corrections, preventing inference errors and maintaining CP correctness.

## Related
- `technique-context-parallel`, `pattern-state-management`, `pattern-async-operations`