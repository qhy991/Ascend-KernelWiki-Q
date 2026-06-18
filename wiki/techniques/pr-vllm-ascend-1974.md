---
id: technique-pr-vllm-ascend-1974
title: "PR Insight: vllm-project/vllm-ascend #1974"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - glibc-abi
  - torch-compatibility
  - vector-core
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1974"
---

# PR Insight: vllm-project/vllm-ascend #1974

**Title:** [Optimize]Change AI Vector core number getting function to glibc ABI free funcition

## Overview
This PR changes the AI Vector core number retrieval function to a glibc ABI-free implementation. This change eliminates glibc ABI problems when bumping the torch version to 2.7.1.

## Technical Significance
Compatibility and portability improvement. Using glibc ABI-free functions ensures better compatibility across different glibc versions and torch versions, reducing deployment friction and potential runtime issues.

## Related
- `technique-torch-compatibility`
- `technique-glibc-abi`
- `hw-vector-unit`