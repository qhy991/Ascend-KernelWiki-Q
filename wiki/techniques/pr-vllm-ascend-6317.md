---
id: technique-pr-vllm-ascend-6317
title: "PR Insight: vllm-project/vllm-ascend #6317"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/6317"
---

# PR Insight: vllm-project/vllm-ascend #6317

**Title:** [bugfix](pcp,gqa) set kv_inverse_idx_for_chunk and cp_kv_recover_idx_for_chunk to None when dcp only

## Overview
This PR fixes a bug in context parallel GQA inference where `kv_inverse_idx_for_chunk` and `cp_kv_recover_idx_for_chunk` should be set to `None` when using only DCP (Decode Context Parallel) without PCP (Prefill Context Parallel). The change was made in `vllm_ascend/attention/context_parallel/attention_cp.py`.

## Technical Significance
The bug was causing incorrect KV index handling in DCP-only scenarios. Since restore and recover operations are only performed for PCP, these indices should be null when only DCP is enabled, preventing memory errors and incorrect attention computation.

## Related
- `technique-context-parallel`
- `technique-gqa`
- `technique-dcp`
- `technique-pcp`