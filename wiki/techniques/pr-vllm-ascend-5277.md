---
id: technique-pr-vllm-ascend-5277
title: "PR Insight: vllm-project/vllm-ascend #5277"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - rotary-embedding
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5277"
---

# PR Insight: vllm-project/vllm-ascend #5277

**Title:** [Refactor] cache cos/sin in mla & remove parameter model in builder.

## Overview
This PR refactors MLA by caching cos/sin rotary embedding values and makes the AttentionBuilder inherit from the original vLLM class. The caching reduces redundant computations and the inheritance removes the unnecessary model parameter from the builder.

## Technical Significance
Caching rotary embedding cos/sin values eliminates redundant computation across attention calls, improving MLA performance. Inheriting from the community AttentionBuilder simplifies code and maintains compatibility with upstream vLLM patterns while preserving Ascend-specific optimizations.

## Related
- technique-mla
- technique-rotary-embedding
- technique-performance-optimization