---
id: technique-pr-vllm-ascend-3799
title: "PR Insight: vllm-project/vllm-ascend #3799"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3799"
---

# PR Insight: vllm-project/vllm-ascend #3799

**Title:** [Test] Add accuracy test for qwen3-8b-w8a8

## Overview
This PR adds accuracy test coverage for Qwen3-8B with W8A8 quantization. It adds a new test configuration file, updates the accuracy test workflow, and modifies the test runner. The CI validation confirms correct inference behavior for this quantized model variant.

## Technical Significance
Comprehensive accuracy testing for quantized models ensures numerical correctness is maintained when using weight/activation quantization. W8A8 (8-bit weights, 8-bit activations) is a common quantization scheme that requires careful handling to maintain model quality. This test prevents regressions in quantization implementations.

## Related
- `technique-testing`
- `technique-quantization`
- `technique-accuracy-validation`