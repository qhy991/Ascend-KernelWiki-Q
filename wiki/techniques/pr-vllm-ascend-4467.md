---
id: technique-pr-vllm-ascend-4467
title: "PR Insight: vllm-project/vllm-ascend #4467"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4467"
---

# PR Insight: vllm-project/vllm-ascend #4467

**Title:** [Attention] add gpt-oss support

**Author:** taoyao1221 | **Merged:** 2026-01-14

## Overview
Adds new functionality for  operations. The feature enhances model capabilities and performance.

## Technical Significance
Attention mechanism optimizations directly impact inference latency, as attention computation is often the bottleneck in transformer models. Improvements here reduce NPU idle time and better utilize the Cube and Vector units for matrix multiplications and softmax operations.

## Related
- `kernel-flash-attention-ascendc`
