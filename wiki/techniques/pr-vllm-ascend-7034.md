---
id: technique-pr-vllm-ascend-7034
title: "PR Insight: vllm-project/vllm-ascend #7034"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sfa
  - lightning-indexer
  - operator-naming
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7034"
---

# PR Insight: vllm-project/vllm-ascend #7034

**Title:** [Bugfix] Resolve operator name collision for DeepSeekV3.2 in RL scena…

## Overview
Fixes operator name collision issues when using DeepSeek-V3.2 with the VERL framework. The ops names in vllm_ascend were identical to CANN operators, causing the training process to invoke ACLNN operators from vllm_ascend instead of intended CANN operators, leading to segmentation faults.

## Technical Significance
Prevents segmentation faults in training scenarios by renaming `sparse_flash_attention` and `lightning_indexer` to `sparse_flash_attention_custom` and `lightning_indexer_custom`. This avoids naming collisions and ensures correct operator dispatch in mixed training/inference environments.

## Related
- `technique-sfa`, `technique-lightning-indexer`, `technique-operator-naming`, `technique-training-inference-mix`