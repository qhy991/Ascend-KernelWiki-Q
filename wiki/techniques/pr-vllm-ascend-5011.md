---
id: technique-pr-vllm-ascend-5011
title: "PR Insight: vllm-project/vllm-ascend #5011"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - rmsnorm
  - quantization
  - graph-pass
  - bias
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5011"
---

# PR Insight: vllm-project/vllm-ascend #5011

**Title:** [Graph][Fusion] Add AddRMSNorm(with bias) and Quant Fusion Pattern

## Overview
This PR adds a graph fusion pass for AddRMSNorm (with bias) and quantization operations. The new norm_quant_fusion_pass.py module implements the fusion pattern in the ACL graph compilation pipeline.

## Technical Significance
Enables fusion of element-wise addition, RMS normalization with bias, and quantization operations into a single kernel, reducing launch overhead and improving memory access patterns.

## Related
- `technique-operator-fusion`
- `kernel-rmsnorm`
- `technique-quantization`
- `kernel-norm-quant-fusion`