---
id: technique-pr-vllm-ascend-7148
title: "PR Insight: vllm-project/vllm-ascend #7148"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - full-mode
  - cudagraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7148"
---

# PR Insight: vllm-project/vllm-ascend #7148

**Title:** [main][bugfix] Fixed the problem of speculative decoding in FULL mode

## Overview
Fixes speculative decoding errors in FULL mode when `num_spec + 1` is not in `cudagraph_capture_sizes`. The fix enables speculative decoding in FULL mode with the drafter running in eager mode, depending on PR #7144.

## Technical Significance
Enables speculative decoding in FULL mode configurations by handling edge cases in CUDA graph capture sizes. The fix allows drafter to run in eager mode when graph capture constraints are not met, maintaining functionality across different deployment scenarios.

## Related
- `technique-spec-decode`, `technique-full-mode`, `technique-cudagraph`, `technique-eager-mode`