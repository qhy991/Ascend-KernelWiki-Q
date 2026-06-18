---
id: technique-pr-vllm-ascend-2581
title: "PR Insight: vllm-project/vllm-ascend #2581"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torchair
  - rotary-embedding
  - refactor
  - rope
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2581"
---

# PR Insight: vllm-project/vllm-ascend #2581

**Title:** [6/N][refactor]delete torchair in rotary ops

## Overview
This PR continues the torchair refactoring by removing torchair-specific code from the main rotary embedding operations. Following the previous move of torchair rope ops into the torchair_ops directory, this removes the torchair dependencies from the core rotary_embedding.py implementation.

## Technical Significance
This refactoring completes the torchair separation by removing torchair-specific code from the general rotary embedding implementation. The cleanup reduces code complexity and improves maintainability by ensuring clear separation between torchair-specific operations and general-purpose rotary embedding functionality. This is part 6 of an N-part refactoring series.

## Related
- `technique-rotary-embedding`
- `technique-torchair`
- `technique-refactor`