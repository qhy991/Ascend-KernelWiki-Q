---
id: technique-pr-modellink-2346
title: "PR Insight: Ascend/ModelLink #2346"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen25
  - training
  - scripts
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2346"
---

# PR Insight: Ascend/ModelLink #2346

**Title:** 添加Qwen2.5 0.5B/1.5B/3B微调脚本

## Overview
This PR adds fine-tuning scripts for smaller Qwen2.5 model variants (0.5B, 1.5B, 3B). These scripts provide configurations for efficient fine-tuning on Ascend hardware.

## Technical Significance
Smaller models require different parallelism strategies than large models. The 0.5B to 3B range may use single-device training or lightweight tensor parallelism. The scripts ensure optimal NPU utilization with proper memory allocation, communication settings, and hyperparameters for each model size, enabling rapid experimentation and fine-tuning on Ascend hardware for edge deployment or research applications.

## Related
- `technique-fine-tuning`
- `technique-distributed-training`