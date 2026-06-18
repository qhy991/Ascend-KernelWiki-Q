---
id: technique-pr-modellink-2452
title: "PR Insight: Ascend/ModelLink #2452"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - attention
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2452"
---

# PR Insight: Ascend/ModelLink #2452

**Title:** [feature] mla zero memory feature

## Overview
This PR implements zero-memory optimization for Multi-head Latent Attention (MLA), a key component of DeepSeek models, reducing memory footprint during attention computation.

## Technical Significance
MLA zero-memory optimization significantly reduces KV cache memory requirements during training, enabling training of larger batch sizes or longer context lengths on fixed hardware. This is particularly important for DeepSeek architecture models.

## Related
- `technique-mla` / `technique-attention` / `technique-memory-optimization`