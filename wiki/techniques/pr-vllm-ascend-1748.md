---
id: technique-pr-vllm-ascend-1748
title: "PR Insight: vllm-project/vllm-ascend #1748"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torchair
  - chunked-prefill
  - mla
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1748"
---

# PR Insight: vllm-project/vllm-ascend #1748

**Title:** [V0.9.1] torchair_graph bugfix when chunked_prefill is true

## Overview
This PR fixes a precision error that occurs when both torchair_graph mode and chunked_prefill are enabled simultaneously. The fix involves properly saving and managing the decode KV cache in the MLA attention implementation at `vllm_ascend/attention/mla_v1.py`.

## Technical Significance
Critical bugfix for correctness in hybrid execution modes. The combination of torchair graph optimization with chunked prefill requires careful KV cache management to avoid precision issues during the transition between prefill and decode phases.

## Related
- `kernel-mla-ascendc`
- `technique-torchair-graph`
- `technique-chunked-prefill`