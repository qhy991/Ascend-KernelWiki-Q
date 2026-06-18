---
id: technique-pr-modellink-2664
title: "PR Insight: Ascend/ModelLink #2664"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2664"
---

# PR Insight: Ascend/ModelLink #2664

**Title:** [mamba] supports mamba2_2.7b from states mamba2.

## Overview
This PR adds support for loading and training the Mamba2 2.7B parameter model from state checkpoints. It enables ModelLink to initialize and continue training Mamba2 models from saved states on Ascend hardware.

## Technical Significance
State loading support is essential for resuming training and transfer learning. Enabling Mamba2 2.7B state loading allows users to leverage pre-trained state-space models and fine-tune them on Ascend NPUs, expanding the capabilities available to researchers and developers.

## Related