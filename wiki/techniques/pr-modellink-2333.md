---
id: technique-pr-modellink-2333
title: "PR Insight: Ascend/ModelLink #2333"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseek3
  - weight-conversion
  - huggingface
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2333"
---

# PR Insight: Ascend/ModelLink #2333

**Title:** deepseek3权重支持mg转hf

## Overview
This PR adds support for converting DeepSeekV3 weights from ModelLink format to HuggingFace format. The conversion enables portability of trained DeepSeekV3 models to the broader ecosystem.

## Technical Significance
Converting DeepSeekV3 weights requires handling MLA compressed KV representations, MoE expert weights, and specialized layer structures. The conversion must preserve numerical accuracy while transforming weight layouts and formats. This support enables deployment of ModelLink-trained DeepSeekV3 models on HuggingFace inference servers, cloud platforms, and other frameworks, increasing accessibility and usability of Ascend-trained models.

## Related
- `kernel-attention-mla`
- `technique-weight-conversion`
- `technique-moe-training`