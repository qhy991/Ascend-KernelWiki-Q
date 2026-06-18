---
id: technique-pr-modellink-2557
title: "PR Insight: Ascend/ModelLink #2557"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - glm
  - training
  - script
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2557"
---

# PR Insight: Ascend/ModelLink #2557

**Title:** add sh of glm_z1_32b_0414

## Overview
This PR adds shell scripts for training the GLM-Z1-32B model (version 0414) on Ascend hardware. GLM is a family of Chinese language models, and this adds training infrastructure support for this specific 32B parameter variant.

## Technical Significance
Adds training support for new GLM model variants on Ascend NPU hardware. These scripts handle distributed training configuration, data preprocessing, and model setup optimized for Ascend architecture.

## Related
- GLM model training
- distributed training scripts