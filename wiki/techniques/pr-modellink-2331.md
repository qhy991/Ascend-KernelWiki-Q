---
id: technique-pr-modellink-2331
title: "PR Insight: Ascend/ModelLink #2331"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseekv3
  - scripts
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2331"
---

# PR Insight: Ascend/ModelLink #2331

**Title:** deepseekV3训练shell脚本更新

## Overview
This PR updates training shell scripts for DeepSeekV3. The changes improve configuration, performance, or reliability of DeepSeekV3 training on Ascend hardware.

## Technical Significance
DeepSeekV3 training scripts must correctly configure MLA attention, MoE expert routing, and distributed training across tensor/pipeline/data parallelism dimensions. Updates may include optimized communication overlap settings, memory management improvements, or corrected hyperparameters for convergence. Proper script configuration is critical for achieving stable training and optimal performance on large Ascend clusters.

## Related
- `kernel-attention-mla`
- `technique-moe-training`
- `technique-distributed-training`