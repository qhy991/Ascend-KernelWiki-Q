---
id: technique-pr-modellink-2745
title: "PR Insight: Ascend/ModelLink #2745"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mamba
  - pipeline
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2745"
---

# PR Insight: Ascend/ModelLink #2745

**Title:** [mamba]Update the pipeline mamba2_2.7b

## Overview
This PR updates the training pipeline for the Mamba2 2.7B model. The updates improve the training efficiency, configuration, or compatibility of the Mamba2 model on Ascend hardware.

## Technical Significance
Mamba2 is a state-space model with different computational patterns than transformers. Updating the pipeline ensures optimal performance on Ascend NPUs by tailoring the training process to the model's unique architecture.

## Related
- technique-operator-fusion