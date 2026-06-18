---
id: technique-pr-vllm-ascend-9867
title: "PR Insight: vllm-project/vllm-ascend #9867"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - spec-decode
  - token-indices
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9867"
---

# PR Insight: vllm-project/vllm-ascend #9867

**Title:** [BugFix][Ascend950][spec decode] Fix draft model index out of range error caused by token_indices_to_sample

## Overview
This PR fixes an index out of range error in speculative decoding draft models on Ascend 950, caused by incorrect handling in `token_indices_to_sample`. The error occurred when draft model token indices exceeded expected bounds.

## Technical Significance
Fixes runtime crashes in spec decode on Ascend 950 by ensuring draft model token indices remain within valid ranges. Prevents out-of-bounds access during draft token generation and validation, improving spec decode reliability.

## Related
- `technique-spec-decode`, `pattern-token-handling`, `pattern-validation`