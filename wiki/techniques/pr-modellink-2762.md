---
id: technique-pr-modellink-2762
title: "PR Insight: Ascend/ModelLink #2762"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2762"
---

# PR Insight: Ascend/ModelLink #2762

**Title:** add script of qwen3-1.7b

## Overview
This PR adds training and evaluation scripts for the Qwen3 1.7B model, a compact language model. The scripts provide configurations for pretraining, tuning, and inference on Ascend hardware.

## Technical Significance
The 1.7B parameter size enables fast training and inference with lower resource requirements. These scripts make it easy to leverage Ascend NPUs for efficient training of smaller models that can be quickly iterated upon.

## Related
- technique-operator-fusion