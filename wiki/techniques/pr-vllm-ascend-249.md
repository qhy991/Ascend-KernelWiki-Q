---
id: technique-pr-vllm-ascend-249
title: "PR Insight: vllm-project/vllm-ascend #249"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
  - cann
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/249"
---

# PR Insight: vllm-project/vllm-ascend #249

**Title:** [Fix] Remove npu_group_topk before CANN version update.

## Overview
This PR removes the npu_group_topk function from fused_moe.py (16 additions, 3 deletions) as a compatibility workaround pending a CANN library update.

## Technical Significance
Similar to PR #242, this removes CANN-dependent code to prevent version conflicts. The function will be re-added after the CANN update provides the necessary operators, showing the tight coupling between vllm-ascend and the Ascend software stack.

## Related
- kernel-moe