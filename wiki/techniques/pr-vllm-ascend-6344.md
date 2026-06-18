---
id: technique-pr-vllm-ascend-6344
title: "PR Insight: vllm-project/vllm-ascend #6344"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/6344"
---

# PR Insight: vllm-project/vllm-ascend #6344

**Title:** [bugfix](CP,MLA) fix wrong slot_mapping of decode for mixed p/d batch

## Overview
This PR fixes incorrect slot_mapping generation in mixed prefill/decode batches for context parallel MLA (Multi-Head Latent Attention). The issue was introduced by a previous refactoring (#5672) that removed -1 padding but didn't properly handle decode slot_mapping in mixed batches.

## Technical Significance
The bug caused incorrect token-to-block mapping in decode phase when using PCP with MLA in mixed PD batches. The fix ensures proper slot_mapping generation for decode operations, preventing memory access errors and incorrect attention computation.

## Related
- `technique-context-parallel`
- `technique-mla`
- `technique-gqa`
- `technique-mixed-pd-batch`