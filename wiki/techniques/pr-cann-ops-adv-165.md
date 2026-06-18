---
id: technique-pr-cann-ops-adv-165
title: "PR Insight: cann-ops-adv #165"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - quantization
  - swin-transformer
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/165"
---

# PR Insight: cann-ops-adv #165 - add swin attetion score quant

## Overview
This PR adds attention score quantization for Swin Transformer, enabling quantized attention computation for vision transformers on Ascend NPUs.

## Technical Significance
Attention score quantization reduces memory bandwidth for Swin Transformer inference, which is critical for vision applications. This operator supports quantized attention score computation, maintaining accuracy while improving performance on Ascend NPUs.

## Related
- `kernel-attention`
- `kernel-quant-matmul`
- `technique-online-softmax`
- `technique-quantization-int8`