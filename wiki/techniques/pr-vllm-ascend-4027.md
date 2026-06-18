---
id: technique-pr-vllm-ascend-4027
title: "PR Insight: vllm-project/vllm-ascend #4027"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/4027"
---

# PR Insight: vllm-project/vllm-ascend #4027

**Title:** [MM][Bugfix] Add MoE verification for multi-modal models (#3897)

## Overview
This PR is the main branch version of PR #3897, fixing MoE model verification for multi-modal models (VL and Omni) by recursively checking the config dict for keys containing "expert". The original `is_moe_model` function only checked text-only models, missing multi-modal MoE models which store configuration in nested `text_config` dictionaries.

## Technical Significance
Proper MoE detection across model types ensures consistent behavior for both text-only and multi-modal models. The recursive config check is more robust than architecture-based detection, working before model loading and enabling proper ACLGraph configuration and MoE communication setup for all model types on Ascend hardware.

## Related
- `technique-moe`, `technique-expert-parallel`, `technique-multi-modal`, `pattern-config-detection`