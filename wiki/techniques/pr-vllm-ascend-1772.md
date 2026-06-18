---
id: technique-pr-vllm-ascend-1772
title: "PR Insight: vllm-project/vllm-ascend #1772"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - chunked-prefill
  - torchair
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1772"
---

# PR Insight: vllm-project/vllm-ascend #1772

**Title:** [Feat] chunkprefill mla support torchair graph

## Overview
This PR enables torchair graph support for chunked-prefill MLA attention, which previously only supported eager mode. The implementation uses torchair graph when all requests are in decode phase, and falls back to eager mode during chunked-prefill or prefill-only phases.

## Technical Significance
Performance optimization for mixed workloads. By selectively using graph mode for decode while keeping eager mode for prefill, this achieves better performance without sacrificing flexibility. The hybrid approach is essential for production serving with variable request patterns.

## Related
- `kernel-mla-ascendc`
- `technique-torchair-graph`
- `technique-chunked-prefill`
- `technique-graph-eager-hybrid`