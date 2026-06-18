---
id: technique-pr-vllm-ascend-9452
title: "PR Insight: vllm-project/vllm-ascend #9452"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - hc-pre
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9452"
---

# PR Insight: vllm-project/vllm-ascend #9452

**Title:** [BugFix][Model] Fix DeepSeek V4 hc_pre op and add 4-card E2E test

## Overview
This PR fixes issues with the DeepSeek V4 hc_pre operation and adds comprehensive 4-card end-to-end tests. The changes affect the model code, build scripts, and test infrastructure to ensure correct behavior and validate the fixes.

## Technical Significance
hc_pre is a critical operation in DeepSeek V4 that affects model accuracy. The fix ensures correct computation, while the 4-card E2E tests validate distributed inference behavior, improving confidence in the implementation for production deployments.

## Related
- `technique-operator-fusion`
- `hw-cube-unit`