---
id: technique-pr-vllm-ascend-5271
title: "PR Insight: vllm-project/vllm-ascend #5271"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - gating
  - aclnn
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5271"
---

# PR Insight: vllm-project/vllm-ascend #5271

**Title:** moe_gating_top_k

## Overview
This PR adds support for the `moe_gating_top_k` custom operator, which enables post-positioned renormalization on top of softmax for MoE expert selection. The implementation includes comprehensive kernel support with tiling, multi-core optimization, and support for quantized and unquantized scenarios.

## Technical Significance
The MoE gating top-k operator is critical for efficient expert routing in Mixture-of-Experts models. The custom implementation provides optimized performance on Ascend NPUs with proper tiling strategies and multi-core execution, enabling fast expert selection while maintaining numerical accuracy for both quantized and unquantized models.

## Related
- technique-moe
- technique-quantization
- technique-expert-routing