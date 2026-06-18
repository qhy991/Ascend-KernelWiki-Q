---
id: technique-pr-vllm-ascend-4860
title: "PR Insight: vllm-project/vllm-ascend #4860"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - top-k-top-p
  - sampling
  - cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4860"
---

# PR Insight: vllm-project/vllm-ascend #4860

**Title:** Remove VLLM_ASCEND_ENABLE_TOPK_TOPP_OPTIMIZATION

## Overview
This PR removes the VLLM_ASCEND_ENABLE_TOPK_TOPP_OPTIMIZATION environment variable, which has been enabled by default for a long time. The code changes affect envs.py and model_runner_v1.py.

## Technical Significance
Simplifies configuration by removing a legacy flag that has become the default behavior. The optimized top_k_top_p operator is now always used without requiring explicit enablement.

## Related
- `kernel-top-k-top-p`
- `technique-sampling-optimization`