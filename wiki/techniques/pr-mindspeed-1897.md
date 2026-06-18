---
id: technique-pr-mindspeed-1897
title: "PR Insight: Ascend/MindSpeed #1897"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - llava
  - tensor-parallel
  - pipeline-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1897"
---

# PR Insight: Ascend/MindSpeed #1897

**Title:** 适配llava ，同时支持tp pp

## Overview
This PR adapts MindSpeed for LLAVA (Large Language-and-Vision Assistant) models and adds support for tensor parallelism (TP) and pipeline parallelism (PP). The changes enable multi-modal model training with efficient parallel execution strategies.

## Technical Significance
Supporting LLAVA extends MindSpeed to vision-language workloads, while TP and PP enable scaling large models across multiple Ascend NPUs. This combination allows efficient training of complex multi-modal models with both spatial and pipeline parallelism.

## Related
- tensor-parallel patterns
- pipeline-parallel patterns
- multi-modal training