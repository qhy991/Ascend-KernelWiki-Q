---
id: technique-pr-vllm-ascend-7470
title: "PR Insight: vllm-project/vllm-ascend #7470"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - qwen3-moe
  - weight-loading
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7470"
---

# PR Insight: vllm-project/vllm-ascend #7470

**Title:** [EPLB][Bugfix] Set parallel_config.enable_eplb to true to load redundant experts

## Overview
This PR fixes an issue where vLLM upstream changes broke EPLB by filtering out redundant experts. The fix uses parallel_config.enable_eplb to determine whether to skip weight loading filtering, temporarily setting it to true when EPLB is enabled.

## Technical Significance
This fix matters for EPLB MoE inference correctness. The upstream change filtered out redundant expert weights, breaking EPLB which needs them for load balancing. By setting enable_eplb during weight loading, the filter is bypassed, ensuring all expert weights are available for EPLB's dynamic expert selection and deployment optimization.

## Related
- technique-eplb
- technique-moe