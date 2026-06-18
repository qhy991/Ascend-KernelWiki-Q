---
id: technique-pr-vllm-ascend-9780
title: "PR Insight: vllm-project/vllm-ascend #9780"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - qkv-split
  - dimension-limit
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9780"
---

# PR Insight: vllm-project/vllm-ascend #9780

**Title:** [BugFix] Chunk wq_b matmul for NPU 65536 dimension limit

## Overview
This PR addresses NPU dimension limits by chunking the wq_b matmul operation when it exceeds the 65536 dimension limit. This prevents execution failures on models with large hidden dimensions that would otherwise exceed NPU constraints.

## Technical Significance
Enables support for models with hidden dimensions exceeding NPU hardware limits by chunking matmul operations into smaller pieces that fit within 65536 dimension constraints. This allows inference of large models that would otherwise fail due to dimension restrictions.

## Related
- `kernel-matmul`, `pattern-qkv-split`, `technique-tiling`