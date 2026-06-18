---
id: technique-pr-modellink-2496
title: "PR Insight: Ascend/ModelLink #2496"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseekv3
  - dualpipe
  - conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2496"
---

# PR Insight: Ascend/ModelLink #2496

**Title:** deepseek3权重转换适配dualpipe

## Overview
This PR adapts DeepSeekV3 (deepseek3) weight conversion for dualpipe (dual pipeline) training. The changes ensure weight compatibility when training DeepSeekV3 using dual pipeline parallelism.

## Technical Significance
DeepSeekV3 uses complex MoE architectures requiring specialized weight partitioning strategies. Dualpipe training adds another dimension to weight distribution. The weight conversion must correctly partition and map weights across pipeline stages while maintaining consistency for training or inference on Ascend NPUs.

## Related
- `technique-pipeline-scheduling`