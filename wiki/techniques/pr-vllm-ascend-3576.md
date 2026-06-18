---
id: technique-pr-vllm-ascend-3576
title: "PR Insight: vllm-project/vllm-ascend #3576"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3576"
---

# PR Insight: vllm-project/vllm-ascend #3576

**Title:** [BugFix]Check all expert maps when using muilty instance.

## Overview
This PR fixes expert map validation for multi-instance MoE (Mixture of Experts) deployments. The fix ensures all expert maps are checked when using multiple instances, addressing scenarios where master and slave instances may have mismatched or missing expert maps. Changes were made to `vllm_ascend/ops/common_fused_moe.py`, `vllm_ascend/ops/expert_load_balancer.py`, and `vllm_ascend/torchair/ops/torchair_fused_moe.py`.

## Technical Significance
Expert maps are critical for MoE inference, determining which expert each token is routed to. In multi-instance deployments, inconsistent expert maps across instances cause incorrect routing or crashes. This fix ensures robust validation by checking all instances' expert maps, tested with Qwen 235B in dual-A3 configurations covering various expert map scenarios.

## Related
- `technique-moe`
- `technique-load-balancing`
- `technique-multi-instance`