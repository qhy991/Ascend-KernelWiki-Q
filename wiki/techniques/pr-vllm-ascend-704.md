---
id: technique-pr-vllm-ascend-704
title: "PR Insight: vllm-project/vllm-ascend #704"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - patch
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/704"
---

# PR Insight: vllm-project/vllm-ascend #704

**Title:** [Bugfix] Fix triton placeholder patch period

## Overview
This PR fixes the Triton placeholder patch timing issue. The triton module replacement was happening too early, causing issues with vLLM initialization on v0.8.4. The fix adjusts when the placeholder is applied.

## Technical Significance
Triton is GPU-only and needs placeholder replacement on Ascend. Incorrect timing causes initialization failures. The fix ensures models load correctly even when Triton kernels are present in the codebase.

## Related
- technique-triton