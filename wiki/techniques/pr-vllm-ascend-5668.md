---
id: technique-pr-vllm-ascend-5668
title: "PR Insight: vllm-project/vllm-ascend #5668"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - medusa
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5668"
---

# PR Insight: vllm-project/vllm-ascend #5668

**Title:** Add Medusa speculative decoding support for vllm_ascend

## Overview
This PR adds Medusa speculative decoding support to vllm_ascend, complementing existing support for MTP, EAGLE, N-gram, and suffix decoding strategies. The implementation includes a new Medusa proposer and integration with the model runner.

## Technical Significance
Expands speculative decoding options by adding Medusa support, which can provide different trade-offs between throughput and latency compared to other strategies. Having multiple speculative decoding methods allows users to choose the best approach for their specific use case and model characteristics.

## Related
- `technique-spec-decode`, `technique-medusa`