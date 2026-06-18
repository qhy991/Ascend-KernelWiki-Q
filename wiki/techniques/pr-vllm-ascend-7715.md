---
id: technique-pr-vllm-ascend-7715
title: "PR Insight: vllm-project/vllm-ascend #7715"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mla
  - sfa
  - memory-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7715"
---

# PR Insight: vllm-project/vllm-ascend #7715

**Title:** [v0.18.0] fix(attention): reuse weight address in graph + RL scenario

## Overview
This PR fixes weight address reuse in MLA v1 and SFA v1 attention implementations for graph execution and reinforcement learning scenarios. The optimization reduces memory allocation overhead.

## Technical Significance
Improves memory efficiency in attention kernels by reusing weight addresses in graph execution and RL workloads, reducing unnecessary memory allocations and improving cache locality.

## Related
- `kernel-mla`, `kernel-sfa`, `kernel-attention`, `technique-memory-reuse`, `pattern-graph-execution`