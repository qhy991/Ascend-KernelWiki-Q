---
id: technique-pr-modellink-2743
title: "PR Insight: Ascend/ModelLink #2743"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen
  - training
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2743"
---

# PR Insight: Ascend/ModelLink #2743

**Title:** support qwen25-7b pretrain, tune ,generate ,evaluate, and pretrain data convert , ckpt convert

## Overview
This PR adds comprehensive support for the Qwen2.5 7B model, including pretraining, fine-tuning, generation, evaluation, pretrain data conversion, and checkpoint conversion. It provides a complete end-to-end pipeline for this model on Ascend hardware.

## Technical Significance
Qwen2.5 7B is a widely used model size. Providing complete support across all training and inference workflows enables developers to leverage Ascend NPUs efficiently for this model, with optimized data processing and checkpoint management.

## Related
- technique-operator-fusion