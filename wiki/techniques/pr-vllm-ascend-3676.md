---
id: technique-pr-vllm-ascend-3676
title: "PR Insight: vllm-project/vllm-ascend #3676"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - qwen3
  - int8
  - e2e
  - feature-stack
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3676"
---

# PR Insight: vllm-project/vllm-ascend #3676

**Title:** [Test] add a new Qwen3-32b-int8 test case with feature_stack3

## Overview
This PR adds a new E2E test case for Qwen3-32B-int8 with feature_stack3 configuration for nightly testing. The test covers performance and accuracy validation of Qwen3-32B-int8 with a new feature. It adds 106 lines to `tests/e2e/nightly/features/test_qwen3_32b_int8_a3_feature_stack3.py` and 11 lines to the nightly workflow configuration.

## Technical Significance
Comprehensive test coverage for new features and configurations is essential for maintaining quality. This test validates both performance and correctness for Qwen3's int8 quantized variant with feature_stack3, ensuring recent optimizations don't introduce regressions. Nightly tests provide continuous validation for production workloads.

## Related
- `technique-testing`
- `technique-quantization`
- `technique-e2e-testing`