---
id: technique-pr-vllm-ascend-6473
title: "PR Insight: vllm-project/vllm-ascend #6473"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rms-norm
  - aclgraph
  - gemma
  - custom-op
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6473"
---

# PR Insight: vllm-project/vllm-ascend #6473

**Title:** Add GemmaRmsNorm ACLGraph Support

## Overview
This PR adds ACLGraph support for Gemma RMS Normalization by introducing a custom NPU operation (npu_gemma_rms_norm) with dynamic shape handling. It includes PyTorch operator registration, meta-implementation for symbolic tracing, and Python frontend integration to replace the generic torch_npu.npu_rms_norm.

## Technical Significance
Enables efficient Gemma model inference on Ascend hardware by providing a specialized RMSNorm operation with ACLGraph optimization support. The custom operator allows for better graph mode performance and dynamic shape handling specific to Gemma's normalization requirements.

## Related
- `technique-layernorm`