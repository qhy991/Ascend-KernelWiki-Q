---
id: technique-pr-vllm-ascend-4826
title: "PR Insight: vllm-project/vllm-ascend #4826"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - async-scheduling
  - e2e-test
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4826"
---

# PR Insight: vllm-project/vllm-ascend #4826

**Title:** add e2e test for mtp async_scheduling

## Overview
This PR adds end-to-end tests for MTP (Multi-Token Prediction) with async_scheduling in tests/e2e/singlecard/test_async_scheduling.py.

## Technical Significance
Improves test coverage for MTP speculative decoding with async scheduling, ensuring correctness and preventing regressions in this critical inference acceleration path.

## Related
- `technique-mtp`
- `technique-async-scheduling`
- `technique-speculative-decoding`