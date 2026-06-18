---
id: technique-pr-vllm-ascend-6981
title: "PR Insight: vllm-project/vllm-ascend #6981"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eagle
  - cp
  - spec-decode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6981"
---

# PR Insight: vllm-project/vllm-ascend #6981

**Title:** [eagle][cp][bugfix] Fix the bug in eagle and cp enabled

## Overview
Fixes errors in `pcp_allgather` when Eagle speculative decoding and context parallelism (CP) are enabled simultaneously. The issue was caused by problems with hidden_states tensor handling in this combined configuration.

## Technical Significance
Enables stable operation of Eagle speculative decoding with context parallelism by fixing tensor communication issues. The fix ensures correct tensor distribution and aggregation across devices in CP scenarios.

## Related
- `technique-eagle`, `technique-cp`, `technique-spec-decode`, `technique-allgather`