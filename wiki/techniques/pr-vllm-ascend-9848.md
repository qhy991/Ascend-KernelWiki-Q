---
id: technique-pr-vllm-ascend-9848
title: "PR Insight: vllm-project/vllm-ascend #9848"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/9848"
---

# PR Insight: vllm-project/vllm-ascend #9848

**Title:** [BugFix][0.20.2] Chunk wq_b matmul for NPU 65536 dimension limit

## Overview
This PR is a backport of the NPU dimension limit fix (#9780) to v0.20.2, addressing the same issue of chunking wq_b matmul operations that exceed the 65536 dimension limit.

## Technical Significance
Ensures production stability by backporting critical dimension limit handling to v0.20.2 release. Prevents execution failures for large models in production deployments using the v0.20.2 branch.

## Related
- `kernel-matmul`, `pattern-qkv-split`, `technique-tiling`