---
id: technique-pr-vllm-ascend-5664
title: "PR Insight: vllm-project/vllm-ascend #5664"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - mrope
  - triton
  - cann-8.5
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5664"
---

# PR Insight: vllm-project/vllm-ascend #5664

**Title:** support triton of mrope

## Overview
This PR adds Triton implementation support for mrope (multi-dimensional rotary positional embedding), matching the performance of AscendC ops. The Triton implementation requires CANN 8.5.0 and provides an alternative to AscendC mrope operations.

## Technical Significance
Provides Triton-based mrope implementation as an alternative to AscendC operators, offering flexibility and potentially easier maintenance. Performance parity with AscendC ops ensures no regression while enabling Triton-based workflows. This is particularly useful for models that use multi-dimensional rotary embeddings.

## Related
- `kernel-rotary-embedding`, `technique-positional-encoding`, `triton`