---
id: technique-pr-modellink-2751
title: "PR Insight: Ascend/ModelLink #2751"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2751"
---

# PR Insight: Ascend/ModelLink #2751

**Title:** add Qwen3 32b scripts

## Overview
This PR adds training, fine-tuning, and evaluation scripts for the Qwen3 32B model. The scripts provide complete pipelines for pretraining, tuning, inference, and evaluation on Ascend hardware.

## Technical Significance
Qwen3 32B is a large-scale model that benefits from Ascend's computational efficiency. The scripts include optimized configurations for memory management, distributed training, and performance tuning specific to Ascend NPUs.

## Related
- technique-operator-fusion