---
id: technique-pr-vllm-ascend-9123
title: "PR Insight: vllm-project/vllm-ascend #9123"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - spec-decode
  - eagle
  - triton
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9123"
---

# PR Insight: vllm-project/vllm-ascend #9123

**Title:** [Test][SpecDecode] Refactor prepare_inputs tests for AscendEagleProposer

## Overview
This PR refactors unit tests for EagleProposer in `tests/ut/spec_decode/test_eagle_proposer.py`, transitioning from unittest style to pytest with fixtures for setup/teardown and standard assert statements. The refactoring includes a new helper function `assert_metadata_attr_equal` for streamlined attribute verification and updated test cases for `prepare_inputs` and `prepare_inputs_padded` with comprehensive data and parametrization for both Triton-enabled and Triton-disabled environments.

## Technical Significance
The pytest migration improves test maintainability and readability while ensuring comprehensive coverage of EagleProposer functionality across different execution environments. The parametrized tests validate the preparatory logic for speculative decoding inputs in both Triton and non-Triton configurations, which is critical for reliable speculative decoding performance.

## Related
- `technique-speculative-decoding`, `kernel-attention-ascendc`