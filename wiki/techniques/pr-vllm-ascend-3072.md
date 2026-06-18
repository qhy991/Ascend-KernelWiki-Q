---
id: technique-pr-vllm-ascend-3072
title: "PR Insight: vllm-project/vllm-ascend #3072"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - nz-format
  - deepseek
  - disagg-prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3072"
---

# PR Insight: vllm-project/vllm-ascend #3072

**Title:** [Feature] Support kv nz feature for DeepSeek decode node in disagg-prefill scenario

## Overview
This PR enables KV cache NZ format support for DeepSeek decode nodes in disaggregated prefill scenarios. By converting KV cache from ND to NZ format when the decode node receives it, the feature works correctly during the decoding phase.

## Technical Significance
NZ format improves memory bandwidth utilization for KV cache access. Supporting NZ format in disaggregated prefill scenarios extends these benefits to distributed inference deployments. The conversion happens at the decode node, ensuring compatibility with the prefill node's ND format.

## Related
- `technique-nz-format`, `technique-kv-cache-paging`, `kernel-deepseek-ascendc`