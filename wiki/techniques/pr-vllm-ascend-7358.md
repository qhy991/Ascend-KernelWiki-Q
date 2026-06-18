---
id: technique-pr-vllm-ascend-7358
title: "PR Insight: vllm-project/vllm-ascend #7358"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - yarn
  - compatibility
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7358"
---

# PR Insight: vllm-project/vllm-ascend #7358

**Title:** [UT] Align input arguments with Ascend(Yarn)RotaryEmbedding with vLLM and add ut

## Overview
This PR adds missing arguments in AscendRotaryEmbedding and AscendYarnRotaryEmbedding to conform with vLLM's interface. It also introduces corresponding unit tests to ensure compatibility with upstream vLLM implementations.

## Technical Significance
This compatibility fix matters for integrating Ascend rotary embeddings with vLLM. The Yarn rotary embedding extension is used by modern LLMs for extended context lengths. Ensuring argument alignment prevents runtime errors when using these models with vLLM-Ascend and enables proper position encoding for long-context inference.

## Related
- pattern-rotary-embedding
- technique-attention