---
id: technique-pr-vllm-ascend-3804
title: "PR Insight: vllm-project/vllm-ascend #3804"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-ops
  - aclnn
  - grouped-matmul
  - swiglu
  - quantization
  - nz-format
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3804"
---

# PR Insight: vllm-project/vllm-ascend #3804

**Title:** [Kernel] add custom op GmmSwigluQuantWeightNzTensorList

## Overview
This PR introduces infrastructure for adding custom CANN `aclnn` operators to vLLM-ascend, enabling users to define and use their own custom operators. The implementation includes a sample custom op `GmmSwigluQuantWeightNzTensorList`, which extends the CANN operator to accept `list[torch.Tensor]` for weight and weight_scale parameters. The PR adds significant CMake build infrastructure, C++ kernel implementations, and Python bindings.

## Technical Significance
Custom operator infrastructure enables community contributions and specialized optimizations beyond core operators. The sample operator demonstrates grouped matrix multiplication with SwiGLU activation and quantized weights in NZ format, a common pattern in large language models. This foundation allows others to contribute optimized kernels for specific workloads.

## Related
- `technique-custom-operators`
- `technique-aclnn`
- `technique-nz-format`
- `technique-swiglu`