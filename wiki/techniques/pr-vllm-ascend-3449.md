---
id: technique-pr-vllm-ascend-3449
title: "PR Insight: vllm-project/vllm-ascend #3449"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - speculative-decoding
  - prefill
  - decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3449"
---

# PR Insight: vllm-project/vllm-ascend #3449

**Title:** [BUGFIX] Mtp torchair pd fix

## Overview
In memory of https://github.com/vllm-project/vllm-ascend/pull/2610

## Technical Significance
Fixes MTP TorchAir PD (parallel disaggregation) issues for correct distributed speculative decoding.

## Related
- `technique-speculative-decoding`
- `technique-kv-cache-paging`
