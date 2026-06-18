---
id: technique-pr-vllm-ascend-1136
title: "PR Insight: vllm-project/vllm-ascend #1136"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - testing
  - deepseek-v2
  - spec-decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1136"
---

# PR Insight: vllm-project/vllm-ascend #1136

**Title:** [CI/UT][Refactor] move e2e spec decode and deepseek acc test to per pr

## Overview
This PR refactors CI workflow by moving deepseek accuracy tests and spec decode e2e tests to run per-PR instead of periodically. This increases CI time (9 min for multi-card, 3 min for single-card) but provides faster feedback. It also removes obsolete test configurations and fixes version conflicts in dependencies.

## Technical Significance
By running critical accuracy tests per-PR, this change improves code quality and catches regressions earlier. The refactoring also simplifies test infrastructure by removing failing V0 MTP tests and aligning with vLLM's testing conventions. This improves overall system reliability for production deployments.

## Related
- `technique-ci`
- `technique-testing`
- `technique-deepseek-v2`