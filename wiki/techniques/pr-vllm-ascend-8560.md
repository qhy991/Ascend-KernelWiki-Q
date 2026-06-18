---
id: technique-pr-vllm-ascend-8560
title: "PR Insight: vllm-project/vllm-ascend #8560"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-ffn-combine
  - xmask
  - feature
  - expert-idx
  - padding
  - w8a8
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8560"
---

# PR Insight: vllm-project/vllm-ascend #8560

**Title:** [Feature]Add xmask feature for dispatch_ffn_combine operator (only for w8a8 branch)

## Overview
This PR adds xactivemask control logic for the dispatch_ffn_combine operator in W8A8 quantization. When xactivemask is set to 0, the expertIdx of the corresponding token is set to expertNum (calculated as tokenPerExpert * EP). In the initrouting module, expertNum is set to tokenPerExpert * EP + 1. For other logic, if expertIdx == expertNum, the token is placed at the end of the sequence. During communication and computation, each device only processes the first tokenPerExpert * EP experts.

## Technical Significance
The xmask feature provides fine-grained control over expert selection and token placement in MoE operations. This enables optimization strategies where certain tokens can be effectively "masked out" or routed to padding experts. The feature is particularly useful for load balancing and performance optimization in quantized MoE deployments.

## Related
- `technique-moe-optimization`
- `technique-quantization`
- `technique-expert-masking`