---
id: technique-pr-vllm-ascend-4066
title: "PR Insight: vllm-project/vllm-ascend #4066"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - dcp
  - aclgraph
  - attention
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4066"
---

# PR Insight: vllm-project/vllm-ascend #4066

**Title:** [Bugfix]fix pcp dcp attn aclgraph

## Overview
This PR fixes a shape issue with multiple batches in DCP-PCP (Decode Context Parallel - Prefill Context Parallel) graph mode scenarios. The bug caused incorrect attention shape handling when both PCP and DCP were enabled with ACLGraph, leading to incorrect results or crashes.

## Technical Significance
The PCP+DCP combination is a powerful optimization for context parallelism, but complex shape interactions can cause bugs. The shape issue in graph mode reveals challenges in handling variable batch sizes across context parallel dimensions. Fixing this enables correct operation of PCP+DCP with ACLGraph, which is critical for performance in distributed inference scenarios.

## Related
- `technique-context-parallel`, `technique-aclgraph`, `technique-attention`, `pattern-shape-handling`