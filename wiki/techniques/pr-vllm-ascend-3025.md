---
id: technique-pr-vllm-ascend-3025
title: "PR Insight: vllm-project/vllm-ascend #3025"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decoding
  - chunked-prefill
  - mla
  - layout
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3025"
---

# PR Insight: vllm-project/vllm-ascend #3025

**Title:** [Bugfix] Fix specdecoding in chunkedprefill scenario

## Overview
This PR fixes a bug in the speculative decoding phase of chunked prefill where it was using an incorrect path. The fix ensures that speculative decoding always uses the TND layout, which is required for correct speculative decoding operation.

## Technical Significance
Correct layout selection is critical for speculative decoding correctness. The TND (Time-Num-Heads-Dim) layout is required for efficient speculative decoding operations. This fix ensures that chunked prefill and speculative decoding work correctly together, enabling performance optimizations without sacrificing correctness.

## Related
- `technique-spec-decoding`, `technique-chunked-prefill`, `kernel-mla-ascendc`