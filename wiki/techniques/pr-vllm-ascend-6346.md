---
id: technique-pr-vllm-ascend-6346
title: "PR Insight: vllm-project/vllm-ascend #6346"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - context-parallel
  - mla
  - gqa
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6346"
---

# PR Insight: vllm-project/vllm-ascend #6346

**Title:** [0.13.0][cherry-pick][bugfix](CP,MLA) fix wrong slot_mapping of decode for mixed p/d batch

## Overview
This is a cherry-pick of PR #6344 to the 0.13.0 branch, fixing the same slot_mapping bug in context parallel MLA for mixed prefill/decode batches.

## Technical Significance
Same as PR #6344 - ensures correct token-to-block mapping in decode phase for PCP with MLA in mixed PD batches on the 0.13.0 release branch.

## Related
- `technique-context-parallel`
- `technique-mla`
- `technique-gqa`
- `technique-mixed-pd-batch`