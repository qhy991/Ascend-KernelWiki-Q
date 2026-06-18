---
id: technique-pr-vllm-ascend-3807
title: "PR Insight: vllm-project/vllm-ascend #3807"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - qwen3
  - w8a8
  - accuracy
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3807"
---

# PR Insight: vllm-project/vllm-ascend #3807

**Title:** [Test] Add accuracy test for qwen3-30b-a3b-w8a8

## Overview
This PR adds accuracy test coverage for Qwen3-30B-A3B with W8A8 quantization. It adds a new test configuration file and updates the accuracy test workflow. The test validates correct inference behavior for this larger quantized model variant, building on the infrastructure from PR #3799.

## Technical Significance
Testing accuracy on larger model sizes like 30B with W8A8 quantization ensures the quantization implementation maintains correctness across model scales. A3B (Ascend 3rd Generation architecture) variants require specific validation, and this test prevents regressions in production deployments of large-scale quantized models.

## Related
- `technique-testing`
- `technique-quantization`
- `technique-accuracy-validation`