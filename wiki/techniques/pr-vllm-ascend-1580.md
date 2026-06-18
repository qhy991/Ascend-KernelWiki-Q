---
id: technique-pr-vllm-ascend-1580
title: "PR Insight: vllm-project/vllm-ascend #1580"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - attention
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1580"
---

# PR Insight: vllm-project/vllm-ascend #1580

**Title:** [Bugfix] Add func `swap_states` to fix MLA attention

## Overview
This PR adds a `swap_states` function to fix MLA attention computation, ensuring correct state management during attention operations.

## Technical Significance
Resolves MLA attention correctness issues by adding proper state swapping logic. The fix ensures that attention state is correctly managed across inference steps, preventing incorrect attention outputs and maintaining accuracy for MLA-based models.

## Related
- `technique-mla`
- `kernel-attention`