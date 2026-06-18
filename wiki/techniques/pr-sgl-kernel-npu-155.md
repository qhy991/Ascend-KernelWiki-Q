---
id: technique-pr-sgl-kernel-npu-155
title: "PR Insight: sgl-project/sgl-kernel-npu #155"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - swiglu
  - quantization
  - activation
  - elementwise
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/155"
---

# PR Insight: sgl-project/sgl-kernel-npu #155

**Title:** impl fused_swiglu_quant with group_list for deepep-low-latency

## Overview
Implements a fused SwiGLU quantization operator with group_list support for DeepEP low-latency scenarios. The implementation adds the `fused_swiglu_quant` operation in `swiglu_quant.py` with extensive optimization for quantized activation functions, improving efficiency in MoE (Mixture of Experts) inference pipelines.

## Technical Significance
This fused operator combines SwiGLU activation with quantization, reducing memory access and kernel launch overhead for low-latency DeepEP inference. The group_list parameter enables flexible quantization across different expert groups, which is critical for MoE models where different experts may have varying quantization requirements. This optimization directly impacts inference latency in DeepEP's low-latency mode.

## Related
- `wiki-kernel-matmul` (SwiGLU involves matrix multiplication)
- `wiki-technique-operator-fusion`
- `wiki-technique-quantization`