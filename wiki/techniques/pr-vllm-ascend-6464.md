---
id: technique-pr-vllm-ascend-6464
title: "PR Insight: vllm-project/vllm-ascend #6464"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dispatch-ffn-combine
  - kernel
  - bugfix
  - swiglu
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6464"
---

# PR Insight: vllm-project/vllm-ascend #6464

**Title:** [bugfix][0.13.0]fix bug in dispatch_ffn_combine kernel

## Overview
This PR fixes a bug in the dispatch_ffn_combine kernel where there was an overflow issue with maxoutputsize in the SwiGLU activation computation. The fix is backported to the 0.13.0 release branch.

## Technical Significance
Fixes an integer overflow issue in the dispatch_ffn_combine kernel that affects SwiGLU activation computations. The overflow could cause incorrect output sizes or memory access violations, leading to incorrect results or crashes in MLP/FFN layers using SwiGLU activation.

## Related
- `kernel-mlp`