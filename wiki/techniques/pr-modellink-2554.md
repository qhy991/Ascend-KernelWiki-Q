---
id: technique-pr-modellink-2554
title: "PR Insight: Ascend/ModelLink #2554"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - glm
  - megatron-to-huggingface
  - script
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2554"
---

# PR Insight: Ascend/ModelLink #2554

**Title:** add:补充glm4-9b-0414 mg2hf 脚本

## Overview
This PR adds scripts for converting GLM4-9B (version 0414) models from Megatron format to HuggingFace format. Model conversion is essential for interoperability between different training frameworks and deployment pipelines.

## Technical Significance
Model conversion scripts enable seamless workflow integration between Megatron-LM training on Ascend hardware and HuggingFace ecosystem for deployment and inference. This supports flexible MLOps pipelines for GLM models.

## Related
- model format conversion
- Megatron-LM integration
- HuggingFace compatibility