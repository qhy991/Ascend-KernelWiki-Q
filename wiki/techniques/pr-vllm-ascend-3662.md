---
id: technique-pr-vllm-ascend-3662
title: "PR Insight: vllm-project/vllm-ascend #3662"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multi-instance
  - expert-load-balancing
  - qwen
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3662"
---

# PR Insight: vllm-project/vllm-ascend #3662

**Title:** [BugFix]Check all expert maps when using muilty instance.

## Overview
This PR fixes expert map validation for multi-instance MoE deployments, extending the fix from #3576. It ensures all expert maps are checked when using multiple instances, addressing scenarios where master and slave instances may have mismatched or missing expert maps. Changes were made to `vllm_ascend/ops/common_fused_moe.py`, `vllm_ascend/ops/expert_load_balancer.py`, and `vllm_ascend/torchair/ops/torchair_fused_moe.py`.

## Technical Significance
This appears to be a refactored version of the #3576 fix, with improved expert load balancer logic. Expert maps are critical for MoE routing, and inconsistent maps across instances cause failures. The fix was tested with Qwen 235B in dual-A3 configurations covering various expert map scenarios, ensuring robust validation across all instances.

## Related
- `technique-moe`
- `technique-load-balancing`
- `technique-multi-instance`