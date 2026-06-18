---
id: technique-pr-modellink-2805
title: "PR Insight: Ascend/ModelLink #2805"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - deepseek
  - llama3
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2805"
---

# PR Insight: Ascend/ModelLink #2805

**Title:** 【mindspore】【sh】add deepseek2_lite/llama2/llama3/glm4

## Overview
This PR adds support for DeepSeek-V2 Lite, Llama2, Llama3, and GLM4 models in the MindSpore backend. It includes scripts and configurations for training these models on Ascend NPUs.

## Technical Significance
Expanding model support increases ModelLink's versatility on Ascend NPUs. These additions enable users to train popular architectures like Llama2/3 and GLM4 using the MindSpore backend, providing more options for large-scale training workflows.

## Related
- `technique-distributed-training`