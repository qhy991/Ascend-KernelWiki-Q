---
id: technique-pr-vllm-ascend-10352
title: "PR Insight: vllm-project/vllm-ascend #10352"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10352"
---

# PR Insight: vllm-project/vllm-ascend #10352

**Title:** [BugFix][UT] Mock AscendConfig in SFA metadata builder tests

## Overview
This PR fixes a unit test isolation issue in `tests/ut/attention/a2/test_sfa_v1.py`. PR #10292 added a new `AscendConfig` field `c8_enable_reshape_optim` and introduced access to this field in `vllm_ascend/attention/sfa_v1.py`. However, the SFA metadata builder tests directly constructed `AscendSFAMetadataBuilder` without initializing or mocking `AscendConfig`, causing tests to fail with `RuntimeError: Ascend config is not initialized`. The fix explicitly mocks `vllm_ascend.attention.sfa_v1.get_ascend_config` and sets the required fields including `c8_enable_reshape_optim = False`.

## Technical Significance
This fix addresses an important test isolation principle: unit tests should not depend on process-global initialization side effects. The SFA metadata builder tests were implicitly relying on global `AscendConfig` state, which made them fragile and dependent on test execution order. By mocking the dependency explicitly, the tests are now self-contained and focused on SFA metadata builder behavior. This pattern improves test reliability and maintainability by making dependencies explicit rather than relying on global state.

## Related
- `technique-testing`
- `technique-test-isolation`