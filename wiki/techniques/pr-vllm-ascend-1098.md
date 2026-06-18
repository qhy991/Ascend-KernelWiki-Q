---
id: technique-pr-vllm-ascend-1098
title: "PR Insight: vllm-project/vllm-ascend #1098"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - nz-format
  - flash-attention
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1098"
---

# PR Insight: vllm-project/vllm-ascend #1098

**Title:** Enable kvcache_nz for the decode process in torchair graph mode

## Overview
This PR enables NZ format for KV cache during the decode process in torchair graph mode, significantly reducing attention computation time for long sequences. The implementation modifies `vllm_ascend/attention/mla_v1.py` and adds configuration support through `additional_config.torchair_graph_config.enable_kv_nz=True`.

## Technical Significance
This optimization delivers approximately 20% performance improvement for attention operations in long-sequence scenarios (tested with batch size 64 and sequence lengths 1k+3k). By leveraging NZ format for KV cache, the PR reduces FA (Flash Attention) computation time from 20.80ms to 19.76ms for DeepSeek models, providing substantial throughput improvements for production inference.

## Related
- `technique-nz-format`
- `technique-kv-cache`
- `technique-flash-attention`
- `technique-deepseek`