---
id: technique-pr-vllm-ascend-6284
title: "PR Insight: vllm-project/vllm-ascend #6284"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - attention
  - fia-operator
  - eagle
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6284"
---

# PR Insight: vllm-project/vllm-ascend #6284

**Title:** [0.13.0][Bugfix] Fix FIA operator validation error in Eagle scenario with CANN 8.5

## Overview
This PR fixes FIA operator validation errors in Eagle speculative decoding scenarios after CANN 8.5 upgrade. The new CANN version requires `queryT` to equal the last element of `actualSequenceLengthQ` when using TND layout, which was failing in Eagle scenarios.

## Technical Significance
The fix adds `_pad_attention_seq_params` function to pad `actual_seq_lengths_q` and `seq_lens` to satisfy the new FIA/TND layout constraints. It ensures compatibility between Eagle speculative decoding and CANN 8.5's stricter validation rules for attention metadata shapes.

## Related
- `technique-attention`
- `technique-eagle`
- `hw-fia-operator`
- `technique-tnd-layout`