---
id: technique-pr-modellink-2662
title: "PR Insight: Ascend/ModelLink #2662"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - glm
  - feature
  - training
  - pretrain
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2662"
---

# PR Insight: Ascend/ModelLink #2662

**Title:** add glm4 32b pretrain

## Overview
This PR adds support for pre-training the GLM4 32B parameter model in ModelLink. It includes the necessary configuration and training scripts to enable pre-training of this large language model architecture on Ascend hardware.

## Technical Significance
GLM4 is a major LLM architecture, and support for its 32B variant enables training of mid-to-large scale models on Ascend NPUs. Pre-training support allows researchers and organizations to build custom models using the GLM4 architecture, expanding the model ecosystem on Ascend platforms.

## Related