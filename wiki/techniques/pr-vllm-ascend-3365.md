---
id: technique-pr-vllm-ascend-3365
title: "PR Insight: vllm-project/vllm-ascend #3365"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3365"
---

# PR Insight: vllm-project/vllm-ascend #3365

**Title:** [MoE] [Refactor] Remove manual memory cleanup

## Overview
1. Replace manual memory cleanup with passing parameter.

## Technical Significance
Removes manual memory cleanup in MoE implementation to simplify memory management and rely on automatic garbage collection.

## Related
- `technique-moe-routing`
