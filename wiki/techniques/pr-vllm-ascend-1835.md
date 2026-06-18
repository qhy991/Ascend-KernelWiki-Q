---
id: technique-pr-vllm-ascend-1835
title: "PR Insight: vllm-project/vllm-ascend #1835"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - v0-deprecation
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1835"
---

# PR Insight: vllm-project/vllm-ascend #1835

**Title:** [Misc][V0 Deprecation] Remove V0 Attention

## Overview
This PR removes the V0 attention implementation as part of issue #1620 which tracks the deprecation of V0 code paths. This is part of the broader migration to V1 attention architecture.

## Technical Significance
Code deprecation and maintenance. Removing V0 attention reduces code complexity and focuses development on the V1 architecture which provides better extensibility and performance characteristics.

## Related
- `kernel-attention-ascendc`
- `technique-v0-deprecation`
- `technique-v1-attention`