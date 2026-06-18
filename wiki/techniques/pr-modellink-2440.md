---
id: technique-pr-modellink-2440
title: "PR Insight: Ascend/ModelLink #2440"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - deepseek
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2440"
---

# PR Insight: Ascend/ModelLink #2440

**Title:** 迁移deepseek3的8机脚本到test/poc/deepseek3下面

## Overview
This PR migrates the 8-machine training scripts for DeepSeek3 models to the test/poc/deepseek3 directory, organizing multi-node training configurations for better accessibility and maintenance.

## Technical Significance
Organized multi-node training scripts provide reference configurations for large-scale distributed training on Ascend clusters, helping users set up 8-machine DeepSeek3 training with proper parallelization and communication settings.

## Related
- `technique-distributed-training` / `technique-deepseek` / `technique-multi-node`