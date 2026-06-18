---
id: technique-pr-vllm-ascend-9795
title: "PR Insight: vllm-project/vllm-ascend #9795"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - dflash
  - mtp
  - lm-head
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9795"
---

# PR Insight: vllm-project/vllm-ascend #9795

**Title:** [BugFix][SpecDecode] Keep draft lm_head for DFlash with reduced (d2t) vocab

## Overview
This PR fixes spec decode with DFlash when using reduced (d2t) vocabulary by ensuring that draft lm_head is kept correctly. The issue occurred when vocabulary reduction was applied to the draft model.

## Technical Significance
Fixes DFlash spec decode compatibility with reduced vocabulary scenarios by preserving draft lm_head appropriately. Enables efficient inference with vocabulary reduction while maintaining speculative decoding functionality.

## Related
- `technique-spec-decode`, `technique-dflash`, `technique-vocab-reduction`