---
id: technique-pr-vllm-ascend-2610
title: "PR Insight: vllm-project/vllm-ascend #2610"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torchair
  - mtp
  - disaggregation
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2610"
---

# PR Insight: vllm-project/vllm-ascend #2610

**Title:** [0.9.1][BUGFIX] [mtp][pd] FIX mtp torchair bug

## Overview
This PR fixes a torchair graph mode bug when running Multi-Token Prediction (MTP) with Prefilling-Decoding (PD) Disaggregation. The issue occurs when all requests processed by the D node are newly transmitted from the P node, causing graph breaking due to FIA operator constraints.

## Technical Significance
The bug fix addresses graph mode padding issues in PD disaggregation scenarios. The root cause is that P nodes transmit only KV cache and prompts, not actual inference tokens, causing D nodes to treat requests as seq_len=1. When torchair graph mode expects padding for 2 tokens per request, all seq_len=1 requests break FIA graph constraints. The solution adds extra torchair graph padding in the KV consumer to avoid breaking graph constraints.

## Related
- `technique-torchair`
- `technique-mtp`
- `technique-disaggregation`