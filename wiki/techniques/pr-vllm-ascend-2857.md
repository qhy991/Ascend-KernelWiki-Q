---
id: technique-pr-vllm-ascend-2857
title: "PR Insight: vllm-project/vllm-ascend #2857"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - qwen
  - torchair
  - eplb
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2857"
---

# PR Insight: vllm-project/vllm-ascend #2857

**Title:** [Bugfix] Retrieve num_redundant_experts from eplb_config in torchair qwen3_moe.py

## Overview
This PR fixes a configuration retrieval issue related to EPLB (Expert Parallel Load Balancing) settings in the torchair qwen3_moe.py implementation, specifically retrieving the num_redundant_experts parameter from the correct configuration location.

## Technical Significance
Bug fix for EPLB configuration retrieval in torchair mode, ensuring that the correct number of redundant experts is used for load balancing. Proper configuration is essential for correct MoE behavior and performance, especially in torchair mode where graph compilation requires accurate parameter values.

## Related
- `kernel-moe-ascendc`, `technique-eplb`, `technique-torchair`