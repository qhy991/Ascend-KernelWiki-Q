---
id: technique-pr-vllm-ascend-2385
title: "PR Insight: vllm-project/vllm-ascend #2385"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-ops
  - rotary-embedding
  - registration
  - out-of-tree
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2385"
---

# PR Insight: vllm-project/vllm-ascend #2385

**Title:** [CustomOp] Register RotaryEmbedding instead of overwrite forward

## Overview
This PR refactors the RotaryEmbedding module architecture by registering it as a named submodule instead of directly overwriting the base class's forward method. The implementation completely rewrites `vllm_ascend/ops/rotary_embedding.py` (272 lines added, 273 lines deleted) and updates tests and initialization code.

## Technical Significance
This architectural change enhances flexibility by making it easier to extend or modify the embedding layer's behavior in the future. Using the proper registration pattern instead of method overwriting aligns with vLLM best practices and reduces potential conflicts with other custom operator implementations.

## Related
- `kernel-rotary-embedding-ascendc`, `technique-custom-ops`, `technique-operator-registration`, `technique-code-refactor`