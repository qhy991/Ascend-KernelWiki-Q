---
id: technique-pr-vllm-ascend-6491
title: "PR Insight: vllm-project/vllm-ascend #6491"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - speculative-decoding
  - accuracy
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6491"
---

# PR Insight: vllm-project/vllm-ascend #6491

**Title:** [bugfix]Fix accuracy issue in PCP/DCP with speculative decoding

## Overview
This PR fixes an accuracy issue when using Prefill/Decode Context Parallelism (PCP/DCP) together with speculative decoding (MTP). The problem is caused by irregular attention mask shapes when both features are enabled, which is resolved by flattening the block_table for speculative decoding requests.

## Technical Significance
Addresses correctness issues in complex inference scenarios combining context parallelism and speculative decoding. The fix ensures regular attention mask shapes by properly handling block_table flattening, preventing incorrect attention computations that would cause accuracy degradation.

## Related
- `technique-speculative-decoding`
- `technique-context-parallel`