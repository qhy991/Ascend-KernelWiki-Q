---
id: technique-pr-vllm-ascend-6472
title: "PR Insight: vllm-project/vllm-ascend #6472"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - graph-mode
  - precompilation
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6472"
---

# PR Insight: vllm-project/vllm-ascend #6472

**Title:** Bugfix: Pre-compile EPLB algorithm successfully in subprocess under graph mode

## Overview
This PR fixes an issue where EPLB (Efficient Paged LRU Buffer) algorithm pre-compilation was failing in subprocesses under graph mode. The fix ensures that kernel pre-compilation procedures run properly in child processes.

## Technical Significance
Fixes a pre-compilation issue that caused runtime performance degradation and stability risks when using graph mode with subprocess-based EPLB execution. The pre-compilation of EPLB algorithms is essential for avoiding runtime compilation overhead during inference.

## Related
- `technique-kv-cache-paging`