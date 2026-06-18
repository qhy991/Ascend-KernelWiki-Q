---
id: technique-pr-vllm-ascend-8755
title: "PR Insight: vllm-project/vllm-ascend #8755"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - vllm
  - ci
  - testing
  - custom-ops
  - qkv
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8755"
---

# PR Insight: vllm-project/vllm-ascend #8755

**Title:** [CI ][Misc] Add timeout check for custom op CI and optimize test parameters

## Overview
This PR improves CI robustness by adding timeout tracking in test configuration. The mechanism tracks test duration and skips subsequent tests in a file if multiple tests exceed timeout thresholds, preventing CI hangs or excessively long-running nightly tests. Additionally, it optimizes the parameter space for `test_fused_qkvzba_split_reshape_cat.py` to reduce overall CI runtime.

## Technical Significance
CI stability is critical for maintaining development velocity and preventing broken builds. Timeout detection prevents individual test failures from blocking the entire pipeline. The custom operator tests (particularly QKV split/reshape/concat operations) are performance-sensitive and can hang on certain configurations. Early termination of test files when multiple tests timeout provides better signal and reduces wasted CI resources.

## Related
- `kernel-attention-ascendc`
- `technique-operator-fusion`