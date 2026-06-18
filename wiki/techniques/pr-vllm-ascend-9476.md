---
id: technique-pr-vllm-ascend-9476
title: "PR Insight: vllm-project/vllm-ascend #9476"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dsa
  - w8a8
  - dynamic
  - bugfix
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9476"
---

# PR Insight: vllm-project/vllm-ascend #9476

**Title:** [BugFix][Attention] Fix DSA v1 W8A8 dynamic conflict

## Overview
This PR fixes a conflict issue with W8A8 dynamic quantization in DSA v1 (DeepSeek Sparse Attention version 1). The fix is implemented in the DSA attention implementation to resolve the conflict and ensure correct behavior with dynamic quantization.

## Technical Significance
DSA v1 with dynamic quantization provides memory-efficient attention but requires proper handling of quantization parameters. The conflict fix ensures correct quantization behavior, preventing incorrect results or crashes when using W8A8 dynamic quantization with DSA v1.

## Related
- `kernel-attention`
- `technique-quantization`