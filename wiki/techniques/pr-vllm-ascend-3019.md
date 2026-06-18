---
id: technique-pr-vllm-ascend-3019
title: "PR Insight: vllm-project/vllm-ascend #3019"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - refactoring
  - code-cleanup
  - redundancy
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3019"
---

# PR Insight: vllm-project/vllm-ascend #3019

**Title:** [1/N][Refactor][Qwen3-Next] remove redundant Qwen3NextSparseMoeBlock and Qwen3NextAttention

## Overview
This PR removes redundant Qwen3NextSparseMoeBlock and Qwen3NextAttention implementations, reducing code duplication and improving maintainability. The change simplifies the Qwen3-Next model implementation by consolidating redundant attention and MoE blocks.

## Technical Significance
Removing redundant code reduces maintenance burden and potential for inconsistencies. The cleanup aligns Qwen3-Next implementation with vLLM community practices, making it easier to sync with upstream changes and reducing the attack surface for bugs.

## Related
- `kernel-qwen3-next-ascendc`, `pattern-code-refactoring`, `kernel-attention-ascendc`