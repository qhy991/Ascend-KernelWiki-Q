---
id: technique-pr-vllm-ascend-3442
title: "PR Insight: vllm-project/vllm-ascend #3442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3442"
---

# PR Insight: vllm-project/vllm-ascend #3442

**Title:** Remove unused row_idx in token_dispatcher

## Overview
The `row_idx` parameter is no longer used since PR[#2689](https://github.com/vllm-project/vllm-ascend/pull/2689), so remove it across multiple files to remove unnecessary calculations and parameter passing.

## Technical Significance
Removes unused row_idx parameter in token dispatcher to simplify MoE token routing logic.

## Related
- `technique-moe-routing`
