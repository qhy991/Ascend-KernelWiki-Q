---
id: technique-pr-vllm-ascend-1732
title: "PR Insight: vllm-project/vllm-ascend #1732"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - topk
  - topp
  - sampler
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1732"
---

# PR Insight: vllm-project/vllm-ascend #1732

**Title:** [Perf] add patch to optimize apply_topk_topp

## Overview
This PR implements a performance optimization for the apply_top_k_top_p sampling operation. The optimization is applied through patches in the sampler module, specifically in `vllm_ascend/patch/worker/patch_common/patch_sampler.py`, and can be enabled via the environment variable `VLLM_ASCEND_ENABLE_TOPK_TOPP_OPTIMIZATION`.

## Technical Significance
Optimizes the critical sampling bottleneck in token generation. The apply_top_k_top_p operation is computationally intensive and affects inference latency. This optimization improves sampling performance without changing user behavior, controlled by an environment variable for safety.

## Related
- `technique-operator-fusion`
- `technique-inference-optimization`