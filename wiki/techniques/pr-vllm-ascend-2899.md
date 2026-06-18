---
id: technique-pr-vllm-ascend-2899
title: "PR Insight: vllm-project/vllm-ascend #2899"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - mooncake
  - distributed
  - pd-separation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2899"
---

# PR Insight: vllm-project/vllm-ascend #2899

**Title:** [P/D][BugFix]Mooncake timeout release bug fix

## Overview
This PR fixes a bug in the Prefill-Decode (PD) separation timeout release mechanism. When KV cache transfers between PD nodes occur too quickly, request IDs could be released twice: first when the decode node notifies the prefill node of KV cache pull completion, and second when the scheduler transmits timeout release to the worker.

## Technical Significance
The fix introduces an intermediate component to manage request ID release timing, preventing double-free errors in distributed inference scenarios. This is critical for correct KV cache management in disaggregated inference systems where prefills and decodes run on separate nodes, as improper request lifecycle management can lead to memory corruption or data loss.

## Related
- `technique-kv-cache-paging`, `technique-distributed-inference`, `pattern-mooncake-connector`