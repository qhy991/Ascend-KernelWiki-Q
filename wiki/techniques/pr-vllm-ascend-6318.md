---
id: technique-pr-vllm-ascend-6318
title: "PR Insight: vllm-project/vllm-ascend #6318"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - context-parallel
  - gqa
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6318"
---

# PR Insight: vllm-project/vllm-ascend #6318

**Title:** [0.13.0][cherry-pick][bugfix](pcp,gqa) set kv_inverse_idx_for_chunk and cp_kv_recover_idx_for_chunk to None when dcp only

## Overview
This is a cherry-pick of PR #6317 to the 0.13.0 branch, fixing the same bug in context parallel GQA inference where KV index recovery parameters should be null when using only DCP without PCP.

## Technical Significance
Same as PR #6317 - prevents incorrect KV index handling and ensures proper memory management in DCP-only scenarios by setting recovery indices to None.

## Related
- `technique-context-parallel`
- `technique-gqa`
- `technique-dcp`
- `technique-pcp`