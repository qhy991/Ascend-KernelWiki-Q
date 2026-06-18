---
id: technique-pr-vllm-ascend-3897
title: "PR Insight: vllm-project/vllm-ascend #3897"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - multi-modal
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3897"
---

# PR Insight: vllm-project/vllm-ascend #3897

**Title:** [MM][Bugfix] Add MoE verification for multi-modal models

## Overview
This PR fixes MoE model verification for multi-modal models (VL and Omni) by recursively checking the config dict for keys containing "expert" instead of only checking text-only model architecture. The original `is_moe_model` function only checked text-only models, missing multi-modal MoE models like Qwen3-VL and Qwen3-Omni which store MoE configuration in nested `text_config` dictionaries.

## Technical Significance
Proper MoE detection is critical for enabling expert parallel and MoE-specific optimizations on Ascend NPUs. The fix ensures that multi-modal MoE models are correctly identified before model loading, enabling proper ACLGraph configuration and MoE communication setup. This is particularly important for large-scale deployments of multi-modal MoE models on Ascend hardware.

## Related
- `technique-moe`, `technique-expert-parallel`, `technique-multi-modal`, `pattern-config-detection`