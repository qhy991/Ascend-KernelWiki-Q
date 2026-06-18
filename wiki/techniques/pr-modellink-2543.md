---
id: technique-pr-modellink-2543
title: "PR Insight: Ascend/ModelLink #2543"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - glm
  - training
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2543"
---

# PR Insight: Ascend/ModelLink #2543

**Title:** add:支持glm4-0414-9b模型

## Overview
This PR adds support for the GLM4-0414-9B model variant to ModelLink. It includes model architecture definitions, configuration, and training/inference support for this specific 9B parameter version of the GLM4 model.

## Technical Significance
Adding support for new GLM4 model variants expands ModelLink's model coverage and enables training and inference of cutting-edge Chinese language models on Ascend hardware. This includes memory optimizations and tensor parallelism support.

## Related
- GLM4 model architecture
- model configuration