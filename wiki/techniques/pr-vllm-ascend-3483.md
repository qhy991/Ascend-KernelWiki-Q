---
id: technique-pr-vllm-ascend-3483
title: "PR Insight: vllm-project/vllm-ascend #3483"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3483"
---

# PR Insight: vllm-project/vllm-ascend #3483

**Title:** Revert "[MoE] [Refactor] Remove manual memory cleanup (#3365)"

## Overview
This reverts commit 4f937f561d573ae97f953169865cfbf70d0c220b.

## Technical Significance
Reverts manual memory cleanup removal in MoE implementation, restoring explicit memory management for stability.

## Related
- `technique-moe-routing`
