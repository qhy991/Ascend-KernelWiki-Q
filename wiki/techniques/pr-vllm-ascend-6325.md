---
id: technique-pr-vllm-ascend-6325
title: "PR Insight: vllm-project/vllm-ascend #6325"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - kv-cache
  - memory-leak
  - pd-disaggregation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6325"
---

# PR Insight: vllm-project/vllm-ascend #6325

**Title:** [bugfix] resolve kv cache leak on P-side due to incorrect req_id

## Overview
This PR fixes a critical KV cache memory leak in the prefill/decode disaggregated pipeline. The issue occurred when KV cache cleanup on the Decode side used the local `req_id` instead of `remote_request_id` to determine the Prefill rank, causing P-side KV cache to remain unreleased.

## Technical Significance
The fix ensures consistent use of `remote_request_id` when determining P-side ranks during cleanup, preventing memory leaks in multi-client scenarios. This is critical for long-running inference services where memory management errors cause gradual performance degradation.

## Related
- `technique-kv-cache`
- `technique-pd-disaggregation`
- `technique-memory-management`
- `technique-mooncake`