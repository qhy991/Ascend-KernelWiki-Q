---
id: technique-pr-modellink-2678
title: "PR Insight: Ascend/ModelLink #2678"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek
  - bugfix
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2678"
---

# PR Insight: Ascend/ModelLink #2678

**Title:** [dskv3]fix mtp_loss in sft and fix mg2hf when having multi mtp

## Overview
This PR fixes issues with DeepSeekV3 MTP (Multi-Token Prediction) loss calculation during SFT (Supervised Fine-Tuning) and resolves problems with the megatron-to-huggingface conversion when dealing with multiple MTP components.

## Technical Significance
MTP is a key technique in DeepSeekV3 for improving generation quality. Correct loss calculation is essential for training, while reliable checkpoint conversion enables model deployment. These fixes ensure accurate training and seamless model export for DeepSeekV3 on Ascend hardware.

## Related
- technique-moe