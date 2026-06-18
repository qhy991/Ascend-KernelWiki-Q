---
id: technique-pr-modellink-2795
title: "PR Insight: Ascend/ModelLink #2795"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen
  - training
  - evaluation
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2795"
---

# PR Insight: Ascend/ModelLink #2795

**Title:** add qwen25_32b pretrain and evaluate

## Overview
This PR adds pre-training and evaluation support for Qwen2.5 32B model in ModelLink. It includes scripts and configurations for these training phases on Ascend NPUs.

## Technical Significance
Adding pre-training and evaluation support enables full training pipeline for Qwen2.5 32B on Ascend NPUs. This allows users to train this mid-sized model from scratch and evaluate performance, expanding platform capabilities.

## Related
- `technique-distributed-training`