---
id: technique-pr-vllm-ascend-782
title: "PR Insight: vllm-project/vllm-ascend #782"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - prefix-cache
  - chunked-prefill
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/782"
---

# PR Insight: vllm-project/vllm-ascend #782

**Title:** [Core] Support the features of prefix cache and chunked prefill in v0/v1

## Overview
This PR enables prefix cache and chunked prefill features in both v0 and v1 engines. The implementation modifies attention and model runner components to support these optimization features that improve long sequence processing efficiency.

## Technical Significance
Prefix caching enables reuse of previously computed key-value across requests, while chunked prefill allows efficient processing of long sequences by breaking them into chunks. Together these features significantly improve inference throughput and memory efficiency for long context workloads on Ascend hardware.

## Related
- `technique-prefix-cache`
- `technique-chunked-prefill`
- `kernel-attention`