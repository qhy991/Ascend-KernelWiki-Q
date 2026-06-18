---
id: technique-pr-vllm-ascend-9221
title: "PR Insight: vllm-project/vllm-ascend #9221"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - mtp
  - bugfix
  - sequence-length
  - drafter
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9221"
---

# PR Insight: vllm-project/vllm-ascend #9221

**Title:** [BugFix]Fix MTP tokens out-of-range error in speculative decoding

## Overview
This PR fixes a bug in speculative decoding where MTP (Multi-Token Prediction) tokens could exceed the drafter's maximum sequence length, causing runtime errors. The fix adds input validation to verify if the input sequence length fits within the drafter's maximum model length and implements a fallback mechanism in padded batch processing logic for oversized inputs.

## Technical Significance
The robustness fix ensures proper token count management and clears draft token buffers when necessary, preventing out-of-range errors when input sequences approach or exceed the drafter's capacity. This is particularly important for MTP scenarios where multiple tokens are predicted simultaneously, as it ensures stable speculative decoding execution across models with varying sequence length constraints.

## Related
- `technique-speculative-decoding`, `kernel-attention-ascendc`, `technique-operator-fusion`