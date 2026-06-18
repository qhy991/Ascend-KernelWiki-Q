---
id: technique-pr-vllm-ascend-179
title: "PR Insight: vllm-project/vllm-ascend #179"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/179"
---

# PR Insight: vllm-project/vllm-ascend #179

**Title:** [MOE] fix #176

## Overview
This PR fixes issue #176 in the MoE operator by setting topk_group and num_expert_group to 0 when they are None. The fix is minimal (2 lines added to fused_moe.py).

## Technical Significance
MoE routing can use grouped expert selection. The None values would cause errors in kernel execution. Defaulting to 0 indicates no grouping is used, maintaining compatibility with models that don't specify these parameters.

## Related
- kernel-moe