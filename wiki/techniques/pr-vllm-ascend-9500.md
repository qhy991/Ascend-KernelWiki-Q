---
id: technique-pr-vllm-ascend-9500
title: "PR Insight: vllm-project/vllm-ascend #9500"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - kv-cache
  - disaggregation
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9500"
---

# PR Insight: vllm-project/vllm-ascend #9500

**Title:** [BugFix]Fix Deepseek-V4 P/D disaggregation kv_cache_tensor.shared_by may be empty

## Overview
This PR fixes an issue where the kv_cache_tensor.shared_by field may be empty in DeepSeek V4 P/D (Prefill/Decode) disaggregation scenarios. The fix is implemented in the Mooncake hybrid connector for KV transfer.

## Technical Significance
P/D disaggregation separates prefill and decode computation across different devices, requiring proper KV cache metadata management. The shared_by field is critical for tracking which devices share KV cache data. Fixing empty values prevents incorrect cache sharing behavior.

## Related
- `kernel-kv-cache`
- `technique-hccl-optimization`