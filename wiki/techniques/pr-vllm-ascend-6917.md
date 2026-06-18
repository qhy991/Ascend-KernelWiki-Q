---
id: technique-pr-vllm-ascend-6917
title: "PR Insight: vllm-project/vllm-ascend #6917"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - chunked-prefill
  - pcp
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6917"
---

# PR Insight: vllm-project/vllm-ascend #6917

**Title:** [feat]ds3.2 pcp support mtp and chunkprefill

## Overview
Enables combination of MTP (Multi-Token Prediction) speculative decoding and chunked prefill features for DeepSeek V3.2 models using Pipeline Context Parallel (PCP). The implementation integrates both optimization strategies to work together in PCP scenarios.

## Technical Significance
Improves DeepSeek V3.2 inference performance by combining speculative decoding with efficient chunked prefill in PCP configurations. This enables better resource utilization and reduced latency for long sequence scenarios.

## Related
- `technique-mtp`, `technique-chunked-prefill`, `technique-pcp`, `technique-spec-decode`