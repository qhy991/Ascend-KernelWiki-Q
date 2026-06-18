---
id: technique-pr-cann-ops-adv-141
title: "PR Insight: cann-ops-adv #141"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - quantization
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/141"
---

# PR Insight: cann-ops-adv #141 - 新增 moeinitroutingquantv2算子

## Overview
This PR adds the MoeInitRoutingQuantV2 operator, which implements quantized version 2 of MoE routing initialization, supporting quantized expert selection for memory-efficient MoE inference.

## Technical Significance
Quantized routing reduces memory bandwidth for expert selection and enables more efficient use of compute resources. This operator supports MoE inference with reduced precision while maintaining routing quality, critical for scaling MoE models on Ascend NPUs.

## Related
- `kernel-moe`
- `kernel-quant-matmul`
- `kernel-topk`
- `technique-quantization-int8`