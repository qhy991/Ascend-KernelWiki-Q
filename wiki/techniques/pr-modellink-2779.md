---
id: technique-pr-modellink-2779
title: "PR Insight: Ascend/ModelLink #2779"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseek
  - bugfix
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2779"
---

# PR Insight: Ascend/ModelLink #2779

**Title:** fix script of deepseek_r1_llama_70b_full

## Overview
This PR fixes training scripts for DeepSeek-R1 Llama 70B full-parameter fine-tuning. It addresses issues with the configuration for this model.

## Technical Significance
DeepSeek-R1 is an important reasoning model. Fixing these scripts enables successful full-parameter fine-tuning on Ascend NPUs, supporting advanced reasoning model development.

## Related
- `technique-distributed-training`