---
id: technique-pr-vllm-ascend-7874
title: "PR Insight: vllm-project/vllm-ascend #7874"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - spec-decode
  - kv-pool
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7874"
---

# PR Insight: vllm-project/vllm-ascend #7874

**Title:** [BugFix][0.18.0][KV Pool] Fix KV Pool not putting kv cache for vllm v0.18.0

## Overview
This PR fixes a bug where KV Pool was not performing Put operations when speculative decoding was enabled in vLLM v0.18. The issue occurred because vLLM v0.18 defers KV connector finalization during target model forward for spec decode, but this change was not carried over to vllm-ascend. The fix adds `finalize_kv_connector` for spec decode scenarios.

## Technical Significance
KV Pool is critical for distributed KV cache management. When spec decode is enabled, the deferred finalization caused KV cache to not be properly stored, breaking cache reuse and multi-instance sharing. This fix ensures that KV Pool works correctly with spec decode, enabling both optimizations to be used together for maximum throughput.

## Related
- `technique-kv-cache-paging`
- `pattern-speculative-decoding`
- `technique-kv-offload`