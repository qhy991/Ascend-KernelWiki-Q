---
id: technique-pr-vllm-ascend-2664
title: "PR Insight: vllm-project/vllm-ascend #2664"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake-connector
  - kv-cache
  - disaggregation
  - timeout
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2664"
---

# PR Insight: vllm-project/vllm-ascend #2664

**Title:** [P/D]mooncake_connector adapted to 0.10.1

## Overview
This PR adapts the mooncake_connector to vLLM 0.10.1, fixing compatibility issues caused by the new KVOutputAggregator in the executor. It adds a policy to forcibly release KV cache when the prefill node times out and refines the connector implementation.

## Technical Significance
The adaptation resolves breaking changes introduced by vLLM 0.10.1's executor restructuring. By adding timeout-based KV cache release and updating communication logic, the PR ensures reliable prefill-decode disaggregation. The significant UT reduction (248 deletions) reflects simplification of communication code.

## Related
- `technique-mooncake-connector`
- `technique-kv-cache`
- `technique-disaggregation`