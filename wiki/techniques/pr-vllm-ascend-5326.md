---
id: technique-pr-vllm-ascend-5326
title: "PR Insight: vllm-project/vllm-ascend #5326"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - eagle
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5326"
---

# PR Insight: vllm-project/vllm-ascend #5326

**Title:** [main][test] Refactor the mtp and eagle test case

## Overview
This PR refactors and expands test cases for MTP (Multi-Token Prediction) and Eagle speculative decoding methods. The refactoring removes redundant tests and adds new necessary test cases to improve coverage and clarity.

## Technical Significance
Comprehensive test coverage for speculative decoding methods ensures correctness of MTP and Eagle implementations on Ascend NPUs. The refactored tests provide better validation of spec decode functionality and catch regressions early in development.

## Related
- technique-mtp
- technique-speculative-decoding
- technique-testing