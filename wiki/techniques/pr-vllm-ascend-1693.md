---
id: technique-pr-vllm-ascend-1693
title: "PR Insight: vllm-project/vllm-ascend #1693"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - rope
  - torchair
  - chunked-prefill
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1693"
---

# PR Insight: vllm-project/vllm-ascend #1693

**Title:** [QuickFix][Rope] Fix rope bug in torchair+chunk-prefill scenario

## Overview
This PR fixes RoPE computation bugs when TorchAir graph mode is combined with chunked-prefill.

## Technical Significance
Resolves incorrect rotary position embedding calculations in the TorchAir+chunk-prefill combination, ensuring correct attention computation. The fix updates MLA V1 attention to properly handle RoPE state across chunk boundaries.

## Related
- `technique-rotary-embedding`
- `technique-torchair`
- `technique-chunked-prefill`