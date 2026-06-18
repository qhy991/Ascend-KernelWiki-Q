---
id: technique-pr-vllm-ascend-1992
title: "PR Insight: vllm-project/vllm-ascend #1992"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - chunked-prefill
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1992"
---

# PR Insight: vllm-project/vllm-ascend #1992

**Title:** [Bug] Fix bug in test_chunked.py

## Overview
This PR fixes bugs in test_chunked.py by removing an incorrect return statement, updating the model from 'deepseek' to 'Qwen2.5-Instruct' for OOM issues in the GitHub e2e test environment, and fixing comparison logic.

## Technical Significance
Test infrastructure maintenance. Fixing test bugs ensures continuous integration stability and prevents false failures that could mask real issues in the codebase.

## Related
- `technique-testing`
- `technique-chunked-prefill`