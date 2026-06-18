---
id: technique-pr-modellink-2605
title: "PR Insight: Ascend/ModelLink #2605"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mamba
  - feature
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2605"
---

# PR Insight: Ascend/ModelLink #2605

**Title:** add convert ckpt of mamba2

## Overview
This PR adds checkpoint conversion support for Mamba2 models. The conversion tool allows users to convert Mamba2 checkpoints between different formats or frameworks, enabling pre-trained models to be used with ModelLink on Ascend hardware.

## Technical Significance
Mamba2 is a state-space model architecture that offers alternatives to Transformers. Checkpoint conversion support enables users to leverage pre-trained Mamba2 models and fine-tune them on Ascend hardware, expanding the model ecosystem available on Ascend NPUs.

## Related