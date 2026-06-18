---
id: technique-pr-vllm-ascend-9528
title: "PR Insight: vllm-project/vllm-ascend #9528"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dispatch-ffn-combine
  - workspace-reuse
  - moe
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9528"
---

# PR Insight: vllm-project/vllm-ascend #9528

**Title:** [Feature]Optimize workspace usage by workspace reuse for dispatch_ffn_combine operator

## Overview
This PR optimizes workspace memory usage for the dispatch_ffn_combine operator by implementing workspace reuse. The changes affect the operator's tiling logic, kernel implementation, and MoE communication methods to reduce memory allocations.

## Technical Significance
Workspace memory can be a significant portion of memory usage for complex operators like dispatch_ffn_combine. Reusing workspace buffers reduces allocation overhead and memory footprint, improving both performance and memory efficiency for MoE inference.

## Related
- `kernel-moe`
- `hw-unified-buffer`
- `technique-data-reuse`