---
id: technique-pr-cann-ops-adv-146
title: "PR Insight: cann-ops-adv #146"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - quantization
  - layernorm
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/146"
---

# PR Insight: cann-ops-adv #146 - add swin_ln_qkv_quant

## Overview
This PR adds the swin_ln_qkv_quant operator, which combines Layer Normalization, Query-Key-Value projection, and quantization for Swin Transformer attention on Ascend NPUs.

## Technical Significance
Fusing LN, QKV projection, and quantization reduces memory bandwidth and kernel launch overhead for Swin Transformer inference. This operator is critical for efficient vision transformer deployment on Ascend NPUs, enabling end-to-end quantized attention.

## Related
- `kernel-attention`
- `kernel-layernorm`
- `kernel-quant-matmul`
- `technique-operator-fusion`