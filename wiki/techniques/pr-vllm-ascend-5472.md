---
id: technique-pr-vllm-ascend-5472
title: "PR Insight: vllm-project/vllm-ascend #5472"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - fullgraph
  - prefill-decode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5472"
---

# PR Insight: vllm-project/vllm-ascend #5472

**Title:** [BugFix] Support ALL D-Nodes in fullgraph when running MTP in PD

## Overview
This PR fixes a critical bug in prefill-decode disaggregation scenarios using MTP speculative decoding with fullgraph compilation and asynchronous scheduling. The issue occurred when decode nodes received KV cache from prefill nodes that didn't include spec tokens, causing full graph enqueueing conditions to fail and mixing full graph and Eagle mode instances, which led to MoE dispatch synchronization bottlenecks.

## Technical Significance
The fix ensures all decode nodes can operate in fullgraph mode by padding spec tokens on decode nodes when KV cache comes from prefill nodes, then rejecting the padded tokens during sampling. This maintains uniformity across decode instances, eliminates MoE dispatch synchronization waits, and preserves the performance benefits of fullgraph compilation in MTP scenarios.

## Related
- `technique-speculative-decoding` (MTP algorithm)
- `technique-fullgraph` (Graph compilation)
- `technique-prefill-decode` (Prefill-decode disaggregation)
- `pattern-moe-dispatch` (MoE dispatch synchronization)