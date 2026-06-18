---
id: technique-pr-vllm-ascend-9235
title: "PR Insight: vllm-project/vllm-ascend #9235"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - bugfix
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9235"
---

# PR Insight: vllm-project/vllm-ascend #9235

**Title:** [BugFix][SpecDecode][v0.18.0] Fix MTP tokens out-of-range error in speculative decoding

## Overview
This PR fixes an out-of-range error in MTP (Multi-Token Prediction) tokens during speculative decoding for v0.18.0. The fix is localized to the model runner implementation, ensuring that token indices remain within valid bounds during the speculative decoding process.

## Technical Significance
Speculative decoding is a critical performance optimization for inference, and MTP extends this by predicting multiple tokens ahead. The fix prevents crashes and incorrect behavior when MTP tokens exceed expected ranges, improving reliability of speculative decoding for models using this optimization.

## Related
- `technique-spec-decode`