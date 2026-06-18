---
id: technique-pr-mindspeed-2209
title: "PR Insight: Ascend/MindSpeed #2209"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - pipeline-parallel
  - refactor
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2209"
---

# PR Insight: Ascend/MindSpeed #2209

**Title:** 重构: 实现pp特性的可变长序列

## Overview
This PR refactors pipeline parallel implementation to support variable-length sequences. The change enables pipeline parallel training with dynamic sequence lengths across batches and micro-batches.

## Technical Significance
Support for variable-length sequences in pipeline parallel is essential for real-world training scenarios where input sequences have varying lengths. This refactoring improves memory efficiency by padding sequences appropriately and handling irregular tensor shapes across pipeline stages. The optimization is particularly important for NLP models with variable-length inputs, enabling efficient training without wasting compute on padding tokens. The implementation likely improves tensor communication and memory management for irregular shapes on Ascend NPUs.

## Related
- `technique-pipeline-scheduling`
- `technique-nz-tiling`