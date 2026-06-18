---
id: technique-pr-vllm-ascend-9367
title: "PR Insight: vllm-project/vllm-ascend #9367"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - kv-cache
  - mtp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9367"
---

# PR Insight: vllm-project/vllm-ascend #9367

**Title:** [BugFix][KVCache] Separate Deepseek-V4 MTP layer KVCache sharding

## Overview
This PR fixes the KV cache sharding logic for DeepSeek V4's MTP (Multi-Token Prediction) layer by implementing separate sharding specifically for MTP layers. The change is in the KV cache utilities patch to ensure proper handling of MTP-specific caching requirements.

## Technical Significance
MTP layers have different caching requirements compared to standard attention layers due to their multi-token prediction nature. Separate sharding ensures correct memory distribution and access patterns, preventing incorrect cache lookups and improving the reliability of MTP inference.

## Related
- `kernel-attention`
- `kernel-kv-cache`