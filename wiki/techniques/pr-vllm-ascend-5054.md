---
id: technique-pr-vllm-ascend-5054
title: "PR Insight: vllm-project/vllm-ascend #5054"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ut
  - pcp
  - dcp
  - attention-cp
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5054"
---

# PR Insight: vllm-project/vllm-ascend #5054

**Title:** [UT]add the UT of pcp and dcp in the attention_cp file

## Overview
This PR adds unit tests for PCP (prefill chunk parallelism) and DCP (decode chunk parallelism) functionality in attention_cp.py.

## Technical Significance
Improves test coverage for context parallelism in attention, preventing regressions in the vectorized PCP/DCP operations.

## Related
- `kernel-attention-cp`
- `technique-context-parallelism`
- `kernel-pcp`
- `kernel-dcp`