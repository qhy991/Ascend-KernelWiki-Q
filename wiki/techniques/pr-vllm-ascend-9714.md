---
id: technique-pr-vllm-ascend-9714
title: "PR Insight: vllm-project/vllm-ascend #9714"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - mtp
  - spec-decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9714"
---

# PR Insight: vllm-project/vllm-ascend #9714

**Title:** [Feature](dsa_cp, MTP) Add MTP support for DSA_CP

## Overview
This PR adds metadata build for drafting in `DSACPMetadataBuilder` to enable DSA_CP with MTP support. It extends the distributed self-attention context parallel implementation to handle multi-token prefix scenarios.

## Technical Significance
Enables MTP (multi-token prefix) functionality with DSA_CP, expanding speculative decoding capabilities. Testing with GSM8K using MTP3 shows stable performance with mean acceptance lengths of 2.89-2.92 tokens and draft acceptance rates of 63.0-63.9% across multiple engine instances.

## Related
- `technique-context-parallel`, `technique-mtp`, `technique-spec-decode`