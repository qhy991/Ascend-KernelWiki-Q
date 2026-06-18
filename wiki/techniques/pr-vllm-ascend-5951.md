---
id: technique-pr-vllm-ascend-5951
title: "PR Insight: vllm-project/vllm-ascend #5951"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - xlite
  - qwen3-moe
  - feature
  - graph-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5951"
---

# PR Insight: vllm-project/vllm-ascend #5951

**Title:** [1/N][Feat] Xlite Qwen3 MoE Support

## Overview
This PR adds support for Qwen3-MoE models in Xlite, including Qwen3-235B-A22B support, Qwen3-MoE weights NZ format support, and Qwen3-MoE data parallel support. Performance comparisons show xlite-decode-only provides significant speedups over aclgraph.

## Technical Significance
Xlite is a graph execution optimization that accelerates inference by fusing operations and reducing overhead. Adding Qwen3-MoE support enables large-scale MoE model inference with graph optimizations. The PR handles weight loading with NZ format and supports data parallelism for distributed deployments. Performance testing on Qwen3-30B-A3B shows xlite-decode-only achieves substantial throughput improvements over aclgraph mode.

## Related
- `technique-xlite`, `technique-qwen3`, `technique-moe`, `technique-nz-format`