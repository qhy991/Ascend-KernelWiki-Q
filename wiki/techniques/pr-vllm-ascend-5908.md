---
id: technique-pr-vllm-ascend-5908
title: "PR Insight: vllm-project/vllm-ascend #5908"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - deepseek-v3
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5908"
---

# PR Insight: vllm-project/vllm-ascend #5908

**Title:** [EPLB][Nightly][Bugfix] Get expert from moe layer only

## Overview
This PR fixes two issues in EPLB: 1) The code incorrectly attempted to obtain routing experts for dense layers, causing errors; 2) The global_expert_map output format affected DeepSeek V3.2 performance. The fix skips dense layers when obtaining routing experts and optimizes the expert map format.

## Technical Significance
Models with both dense and MoE layers (like DeepSeek V3.1) need to distinguish between layer types when extracting routing information. Attempting to get experts from dense layers caused runtime errors. The fix properly filters for MoE layers only. Additionally, optimizing the global_expert_map format improves DeepSeek V3.2 performance. Testing shows DeepSeek V3.1 conversation works correctly and AIME2024 accuracy improves from 66.67% (baseline without EPLB) to 70.00% (with EPLB).

## Related
- `technique-eplb`, `technique-expert-parallel`, `technique-deepseek-v3`