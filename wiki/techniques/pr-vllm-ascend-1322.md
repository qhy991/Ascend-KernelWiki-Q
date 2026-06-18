---
id: technique-pr-vllm-ascend-1322
title: "PR Insight: vllm-project/vllm-ascend #1322"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - multistream
  - dp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1322"
---

# PR Insight: vllm-project/vllm-ascend #1322

**Title:** Handle with_prefill_across_dp for multistream mla

## Overview
This PR adds support for `with_prefill_across_dp` (prefill across data parallel) in multistream MLA (Multi-Head Latent Attention) scenarios.

## Technical Significance
Enables prefill workload distribution across data parallel ranks for MLA in multistream mode, improving resource utilization and throughput. The implementation updates MLA V1 and DeepSeek V2 model files to handle cross-DP prefill correctly, ensuring correct attention computation when prefill spans multiple devices.

## Related
- `technique-mla`
- `technique-multistream`
- `kernel-attention`