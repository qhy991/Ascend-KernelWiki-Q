---
id: technique-pr-vllm-ascend-4160
title: "PR Insight: vllm-project/vllm-ascend #4160"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - mtp
  - testing
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4160"
---

# PR Insight: vllm-project/vllm-ascend #4160

**Title:** [BugFix] adapted e2e tests for Qwen3-next-mtp

## Overview
This PR adapts e2e tests for Qwen3-Next MTP after chunked prefill and splitfuse were enabled by default in PR #3967. The e2e test for MTP broke because a triton operator does not support chunked prefill. The fix modifies the test to only test cases where chunked prefill is disabled, maintaining test coverage without breaking on unsupported configurations.

## Technical Significance
When default configurations change (chunked prefill enabled), tests that relied on previous defaults break. Rather than skipping tests entirely, the fix adapts tests to cover supported configurations, maintaining coverage. This reveals dependencies between features (MTP + chunked prefill) that need resolution for full compatibility.

## Related
- `technique-mtp`, `technique-chunk-prefill`, `technique-qwen3-next`, `pattern-testing`, `pattern-feature-compatibility`