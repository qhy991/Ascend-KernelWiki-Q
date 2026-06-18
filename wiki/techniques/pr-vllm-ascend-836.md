---
id: technique-pr-vllm-ascend-836
title: "PR Insight: vllm-project/vllm-ascend #836"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - torchair
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/836"
---

# PR Insight: vllm-project/vllm-ascend #836

**Title:** [aclgraph] implentment NPUPiecewiseBackend to enable aclgraph

## Overview
This PR implements `NPUPiecewiseBackend` to enable aclgraph mode by default in V1 engine. It includes error handling for DeepSeek models (not supported in graph mode) and warnings for non-Qwen models, with comprehensive unit tests.

## Technical Significance
Aclgraph mode enables TorchAir graph compilation for better performance on Ascend hardware. The piecewise backend allows selective graph compilation of operators while maintaining compatibility with different model architectures. This is a key optimization for inference workloads.

## Related
- `technique-aclgraph`
- `technique-torchair`
- `kernel-inference`