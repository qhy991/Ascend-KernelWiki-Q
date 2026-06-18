---
id: technique-pr-vllm-ascend-9536
title: "PR Insight: vllm-project/vllm-ascend #9536"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - moe
  - metrics
  - observability
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9536"
---

# PR Insight: vllm-project/vllm-ascend #9536

**Title:** [Feature][EPLB] Expose experts hotness metrics data and eplb time consuming

## Overview
This PR adds observability features to the EPLB (Expert Parameter Load Balancing) system by exposing experts hotness metrics data and EPLB time consumption information. The implementation updates EPLB core components and the model runner to collect and expose these metrics.

## Technical Significance
Expert hotness metrics provide visibility into which experts are being used most frequently, enabling better load balancing and routing decisions. Time consumption metrics help identify performance bottlenecks in the EPLB system. Together, these observability features enable better optimization and debugging of MoE inference.

## Related
- `kernel-moe`
- `technique-hccl-optimization`