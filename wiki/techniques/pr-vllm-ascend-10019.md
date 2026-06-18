---
id: technique-pr-vllm-ascend-10019
title: "PR Insight: vllm-project/vllm-ascend #10019"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-transfer
  - mooncake
  - pcp
  - handshake
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10019"
---

# PR Insight: vllm-project/vllm-ascend #10019

**Title:** [BugFix] Fix PCP handshake port collision in Mooncake layerwise KV transfer connector

## Overview
This PR fixes port collision issues during PCP (prefill context parallel) handshake in the Mooncake layerwise KV transfer connector. The issue caused connection failures due to port conflicts in distributed setups.

## Technical Significance
Fixes distributed KV transfer reliability by preventing PCP handshake port collisions in Mooncake layerwise connector. Ensures that PCP communication succeeds without port conflicts, improving distributed inference stability.

## Related
- `technique-context-parallel`, `technique-kv-cache-paging`, `technique-mooncake`, `pattern-communication`