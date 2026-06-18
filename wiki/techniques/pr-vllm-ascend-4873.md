---
id: technique-pr-vllm-ascend-4873
title: "PR Insight: vllm-project/vllm-ascend #4873"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - revert
  - gatingtopk
  - qwen3
  - precision
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4873"
---

# PR Insight: vllm-project/vllm-ascend #4873

**Title:** Revert "[refactor]support gatingtopk operator generalization (#4356)"

## Overview
This PR reverts commit c4a11a745ae638fb160220639afa7887123bc0d5 which generalized the gatingtopk operator. The reversion is due to precision problems caused by npu_gating_top_k in Qwen3-30B models.

## Technical Significance
Rollback of a refactor that caused accuracy issues. The npu_gating_top_k operator's generalization introduced precision errors that need to be addressed before the generalization can be re-applied.

## Related
- `kernel-gatingtopk`
- `kernel-qwen3`
- `technique-moe-routing`