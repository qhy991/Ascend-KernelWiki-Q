---
id: technique-pr-vllm-ascend-5168
title: "PR Insight: vllm-project/vllm-ascend #5168"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - kv-cache
  - kvpool
  - mla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5168"
---

# PR Insight: vllm-project/vllm-ascend #5168

**Title:** [KVPOOL]decode save kvcache

## Overview
This PR implements KV cache saving functionality during decode phase for the KV pool feature, currently supporting MLA (Multi-head Latent Attention) models. The decode-stage KV cache saving enables persistent storage of computed KV pairs for reuse across requests.

## Technical Significance
KV cache persistence during decode phases enables cross-request cache reuse, dramatically reducing computation for repeated prompts or similar contexts. This optimization is particularly valuable for MLA models on Ascend NPUs where KV cache dominates memory footprint and compute cost.

## Related
- technique-kv-cache-paging
- technique-mla
- technique-cross-request-cache