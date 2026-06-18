---
id: technique-pr-modellink-2532
title: "PR Insight: Ascend/ModelLink #2532"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseekv3
  - mindspore
  - script
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2532"
---

# PR Insight: Ascend/ModelLink #2532

**Title:** 新增启动mindspore 支持deepseekv3 shell脚本 与用户文档

## Overview
This PR adds shell scripts and user documentation for launching MindSpore training for DeepSeekV3 models. The changes enable MindSpore backend support specifically for the DeepSeekV3 architecture.

## Technical Significance
DeepSeekV3 is a state-of-the-art MoE model with complex requirements. Adding MindSpore support expands framework compatibility and provides users with alternative backend options. The scripts likely handle MindSpore-specific configurations, distributed training setups, and environment preparation on Ascend hardware.

## Related
- `technique-moe`