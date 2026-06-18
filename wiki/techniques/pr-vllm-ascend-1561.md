---
id: technique-pr-vllm-ascend-1561
title: "PR Insight: vllm-project/vllm-ascend #1561"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - multistream
  - w8a8-dynamic
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1561"
---

# PR Insight: vllm-project/vllm-ascend #1561

**Title:** [Perf][MoE] Improve shared experts multi-stream for w8a8 dynamic

## Overview
This PR improves multistream performance for shared experts in W8A8 dynamic quantized MoE models.

## Technical Significance
Optimizes shared experts computation in multistream mode for W8A8 dynamic quantization, improving resource utilization across concurrent requests. The improvements touch DeepSeek V2 model, fused MoE operator, and W8A8 dynamic quantization components.

## Related
- `kernel-moe`
- `technique-w8a8-quantization`
- `technique-multistream`