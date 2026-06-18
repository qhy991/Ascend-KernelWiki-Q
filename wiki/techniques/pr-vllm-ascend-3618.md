---
id: technique-pr-vllm-ascend-3618
title: "PR Insight: vllm-project/vllm-ascend #3618"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - attribute-error
  - q-proj
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3618"
---

# PR Insight: vllm-project/vllm-ascend #3618

**Title:** [Fix] Fixes attribute error in MLA implementation

## Overview
This PR is the main branch version of the MLA attribute error fix, correcting device attribute access from `q_a_proj` to `q_proj` in `vllm_ascend/attention/mla_v1.py`. It also removed 19 lines from test files, likely cleaning up unused test code related to the MLA implementation.

## Technical Significance
This is a duplicate fix of #3617 for the main branch, addressing the same MLA attribute access error. Proper attribute references are fundamental to correct device allocation in MLA attention. The test cleanup suggests the removed tests were either redundant or broken due to the bug being fixed.

## Related
- `technique-mla`
- `technique-attention`
- `technique-kv-cache-compression`