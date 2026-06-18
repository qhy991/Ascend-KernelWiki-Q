---
id: technique-pr-modellink-2754
title: "PR Insight: Ascend/ModelLink #2754"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen3
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2754"
---

# PR Insight: Ascend/ModelLink #2754

**Title:** [Qwen3]add 8b scripts

## Overview
This PR adds complete training scripts for the Qwen3 8B model, including configurations for pretraining, fine-tuning, inference, and evaluation. The scripts are optimized for Ascend hardware.

## Technical Significance
The 8B parameter size is an efficient middle ground between capability and resource requirements. These scripts enable efficient training of Qwen3 8B on Ascend NPUs with appropriate parallelism strategies and performance optimizations.

## Related
- technique-operator-fusion