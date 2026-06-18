---
id: technique-pr-vllm-ascend-6505
title: "PR Insight: vllm-project/vllm-ascend #6505"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - nz-format
  - test-fix
  - bf16
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6505"
---

# PR Insight: vllm-project/vllm-ascend #6505

**Title:** [Nightly][BugFix] Remove kv_cache nz test case for test_mla_preprocess_nq.py

## Overview
This PR removes a kv_cache NZ format test case from test_mla_preprocess_nq.py that was added but not tested for bf16 scenarios. Testing revealed that NZ format support is not currently available for these cases.

## Technical Significance
Removes invalid test coverage that was testing unsupported functionality. The cleanup ensures test suites accurately reflect actual capabilities and prevents false positive/negative results.

## Related
- `technique-nz-format`