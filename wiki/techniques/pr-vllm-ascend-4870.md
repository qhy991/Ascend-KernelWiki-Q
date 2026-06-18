---
id: technique-pr-vllm-ascend-4870
title: "PR Insight: vllm-project/vllm-ascend #4870"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - refactor
  - attention-mask
  - singleton
  - pcp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4870"
---

# PR Insight: vllm-project/vllm-ascend #4870

**Title:** [Refactor] Fix AttentionMaskBuilder singleton and remove redundant pcp_prefill_mask

## Overview
This PR fixes the AttentionMaskBuilder singleton initialization issue introduced in PR #4779, where two initialization sites were still using the old parameterless constructor instead of the device-aware constructor. It also removes the unused pcp_prefill_mask field from AscendPrefillContextParallelMetadata.

## Technical Significance
Completes the singleton pattern refactoring for AttentionMaskBuilder by fixing constructor calls and removing dead code. This ensures consistent mask generation behavior across attention modules and simplifies the metadata structure.

## Related
- `kernel-attention-mask`
- `technique-singleton-pattern`
- `technique-context-parallelism`