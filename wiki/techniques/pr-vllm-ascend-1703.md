---
id: technique-pr-vllm-ascend-1703
title: "PR Insight: vllm-project/vllm-ascend #1703"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mc2
  - prefill
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1703"
---

# PR Insight: vllm-project/vllm-ascend #1703

**Title:** add chunk mc2 for prefill

## Overview
This PR extends chunk MC2 (Model-Controller-Compute) support to attention operations during prefill phase.

## Technical Significance
Enables MC2 chunking for attention in prefill, improving resource utilization for long prompt processing. The implementation updates MLA attention, forward context, environment configuration, and quantization components to support MC2 patterns.

## Related
- `technique-chunked-prefill`
- `technique-mc2`
- `kernel-attention`