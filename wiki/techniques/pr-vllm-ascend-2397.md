---
id: technique-pr-vllm-ascend-2397
title: "PR Insight: vllm-project/vllm-ascend #2397"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - header-include
  - compatibility
  - cann-toolkit
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2397"
---

# PR Insight: vllm-project/vllm-ascend #2397

**Title:** [Bugfix] Fix header include issue in rope

## Overview
This PR removes incompatible header file includes from the rope implementation to ensure safety when upgrading CANN toolkits. The change removes 5 lines from `csrc/kernels/pos_encoding_kernels.cpp` that included headers not meant for external users.

## Technical Significance
This compatibility fix ensures that vLLM-Ascend's rope implementation won't break when CANN toolkits are updated. By removing internal header includes that may change between toolkit versions, the code becomes more stable and easier to maintain across different CANN releases.

## Related
- `kernel-rotary-embedding-ascendc`, `kernel-rope`, `technique-header-management`, `technique-compatibility`