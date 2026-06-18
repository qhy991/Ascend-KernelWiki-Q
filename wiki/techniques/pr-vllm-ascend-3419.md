---
id: technique-pr-vllm-ascend-3419
title: "PR Insight: vllm-project/vllm-ascend #3419"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - attention
  - hccl-optimization
  - speculative-decoding
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3419"
---

# PR Insight: vllm-project/vllm-ascend #3419

**Title:** bugfix for mtp with multistream_moe

## Overview
when infer deepseek mtp layer with multistream_moe, we should pass a boolean to evaluate this feature and fix bugs when we are  in mtp layer

## Technical Significance
Fixes MTP bugs when using multi-stream MoE for improved speculative decoding stability.

## Related
- `hw-cube-unit`
- `technique-moe-routing`
- `technique-speculative-decoding`
