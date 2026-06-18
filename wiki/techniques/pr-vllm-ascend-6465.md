---
id: technique-pr-vllm-ascend-6465
title: "PR Insight: vllm-project/vllm-ascend #6465"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/6465"
---

# PR Insight: vllm-project/vllm-ascend #6465

**Title:** [bugfix]fix some bug in dispatch_ffn_combine kernel

## Overview
This PR fixes bugs in the dispatch_ffn_combine kernel, specifically addressing maxoutputsize overflow issues in the SwiGLU activation section of the kernel.

## Technical Significance
Fixes integer overflow bugs in the dispatch_ffn_combine kernel's SwiGLU computation path. The overflow could cause incorrect buffer size calculations leading to memory corruption or incorrect results in MLP/FFN layers, particularly important for models using SwiGLU activation functions.

## Related
- `kernel-mlp`