---
id: technique-pr-sgl-kernel-npu-161
title: "PR Insight: sgl-project/sgl-kernel-npu #161"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tree-attention
  - triton
  - speculation
  - new-operator
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/161"
---

# PR Insight: sgl-project/sgl-kernel-npu #161

**Title:** [New Ops] build tree efficient

## Overview
Implements an efficient build tree operator for speculative decoding in large language models. This new operator optimizes the tree construction process for speculative inference, improving performance by profiling and optimizing the tree building kernel on Ascend NPU.

## Technical Significance
The build tree operation is critical for speculative decoding efficiency in LLM inference. This implementation provides significant performance improvements for tree construction, which is a bottleneck in speculative decoding pipelines. The kernel is optimized for Ascend architecture with efficient memory access patterns and computational scheduling, directly impacting speculative decoding throughput and latency.

## Related
- `wiki-kernel-attention`
- `wiki-technique-speculative-decoding`
- `wiki-pattern-tree-attention`
- `wiki-language-triton`