---
id: technique-pr-modellink-2217
title: "PR Insight: Ascend/ModelLink #2217"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - memory-optimization
  - moe
  - dense
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2217"
---

# PR Insight: Ascend/ModelLink #2217

**Title:** [mcore-llm]修复dense/moe场景下的异常显存峰值问题

## Overview
Fixes abnormal GPU memory peak issues in mcore-llm for both dense and MoE model scenarios. The bug was causing unexpected memory spikes during training that could lead to out-of-memory errors.

## Technical Significance
Critical bugfix that prevents out-of-memory errors during training by addressing abnormal memory peaks. This is especially important for large-scale training on memory-constrained Ascend NPU devices, where memory efficiency is crucial.

## Related
- technique-moe
- technique-data-reuse