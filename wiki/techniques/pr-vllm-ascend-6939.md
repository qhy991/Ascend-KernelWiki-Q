---
id: technique-pr-vllm-ascend-6939
title: "PR Insight: vllm-project/vllm-ascend #6939"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - spec-decode
  - mtp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6939"
---

# PR Insight: vllm-project/vllm-ascend #6939

**Title:** [Ops][BugFix] Fix RoPE shape mismatch for mtp models with flashcomm v1 enabled

## Overview
Fixes RoPE shape mismatch errors in draft models using shared expert data parallelism with flashcomm v1 enabled. The positions tensor has incorrect shape for this configuration in models like GLM-4.7. The fix adds a check in `AscendRotaryEmbedding.forward_oot` to process positions tensor using `torch.ops.vllm.maybe_all_gather_and_maybe_unpad` for draft models with shared expert DP.

## Technical Significance
Resolves shape mismatch errors in rotary embedding calculations for speculative decoding with expert parallelism. The fix ensures correct tensor shapes before applying rotary embedding, preventing failures in MTP scenarios with shared expert data parallelism.

## Related
- `technique-rope`, `technique-mtp`, `technique-spec-decode`, `technique-expert-parallelism`