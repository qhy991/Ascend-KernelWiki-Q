---
id: technique-pr-vllm-ascend-3774
title: "PR Insight: vllm-project/vllm-ascend #3774"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - memory-leak
  - weak-references
  - decode-graph
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3774"
---

# PR Insight: vllm-project/vllm-ascend #3774

**Title:** [v0.11.0][Fix] Prevent memory leak in MLA decode graph (#3743)

## Overview
This is a cherry-pick of PR #3743 to the v0.11.0 branch, fixing MLA decode graph memory leaks. The cache was holding strong references to tensors, preventing garbage collection. The fix wraps cached tensors in weak references, allowing deallocation when no longer in use.

## Technical Significance
Backporting memory leak fixes to release branches prevents OOM failures in production. Weak references allow proper memory management while maintaining graph reuse benefits, critical for long-running inference services using MLA-based models.

## Related
- `technique-mla`
- `technique-memory-management`
- `technique-decode-graph`