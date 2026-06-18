---
id: technique-pr-vllm-ascend-706
title: "PR Insight: vllm-project/vllm-ascend #706"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - mla
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/706"
---

# PR Insight: vllm-project/vllm-ascend #706

**Title:** [Feature] Use reshape_and_cache fused op

## Overview
This PR replaces torch functions with the reshape_and_cache fused operator in MLA attention for better performance. The fix addresses a dtype mismatch where the fused op expected int32 but received int64 tensors.

## Technical Significance
Fused operators reduce kernel launch overhead and memory movement. The reshape_and_cache op is critical for KV cache operations. The dtype fix ensures compatibility with MLA's tensor shapes.

## Related
- technique-operator-fusion
- technique-mla