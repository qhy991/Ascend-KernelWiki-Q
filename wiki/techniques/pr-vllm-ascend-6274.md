---
id: technique-pr-vllm-ascend-6274
title: "PR Insight: vllm-project/vllm-ascend #6274"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - quantization
  - rmsnorm
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6274"
---

# PR Insight: vllm-project/vllm-ascend #6274

**Title:** [Fusion] Add rmsnorm dynamic quant fusion pass

## Overview
This PR introduces a fusion pass to combine RMSNorm and DynamicQuant operators into a single fused operator. The implementation adds four new fusion patterns in `vllm_ascend/compilation/passes/norm_quant_fusion_pass.py`, reducing execution time from 22.8us to 16.9us on v0.14.1.

## Technical Significance
This optimization fuses two commonly used operators in inference pipelines (normalization and quantization), reducing kernel launch overhead and improving performance. The fusion pass is particularly important for deployment scenarios where dynamic quantization is applied alongside layer normalization.

## Related
- `technique-operator-fusion`
- `technique-quantization`
- `kernel-rmsnorm`
- `kernel-quantization`