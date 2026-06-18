---
id: technique-pr-vllm-ascend-6348
title: "PR Insight: vllm-project/vllm-ascend #6348"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - e2e-test
  - sampling
  - custom-kernel
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6348"
---

# PR Insight: vllm-project/vllm-ascend #6348

**Title:** [Misc][Test] add e2e test for apply_top_k_top_p_custom kernel

## Overview
This PR adds end-to-end test coverage for the `apply_top_k_top_p_custom` sampling kernel and removes Chinese comments from the kernel implementation. The test was added in `tests/e2e/nightly/single_node/ops/singlecard_ops/test_apply_top_k_top_p_custom.py`.

## Technical Significance
The test validates correctness of the custom top-k/top-p sampling implementation on Ascend hardware. Code cleanup (removing Chinese comments) improves codebase maintainability for international development teams.

## Related
- `technique-sampling`
- `technique-custom-kernel`
- `technique-e2e-testing`