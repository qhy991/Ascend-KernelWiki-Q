---
id: technique-pr-vllm-ascend-6680
title: "PR Insight: vllm-project/vllm-ascend #6680"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - test-fix
  - triton
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6680"
---

# PR Insight: vllm-project/vllm-ascend #6680

**Title:** [Test][BugFix] Fix torch.rand usage in triton penalty test

## Overview
This PR fixes a TypeError in test_penality.py where torch.rand() was incorrectly called with the device string as a positional argument. The fix changes it to use the device keyword argument as intended.

## Technical Significance
Fixes test infrastructure to prevent false test failures. The correction ensures proper torch.rand() usage for device specification, making tests more reliable.

## Related
- `technique-triton`