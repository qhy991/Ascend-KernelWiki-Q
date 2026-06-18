---
id: technique-pr-modellink-2460
title: "PR Insight: Ascend/ModelLink #2460"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - moe
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2460"
---

# PR Insight: Ascend/ModelLink #2460

**Title:** 【BugFix】Mixtral OOM

## Overview
This PR fixes an out-of-memory (OOM) issue when training Mixtral models, likely by optimizing memory allocation, gradient checkpointing, or tensor parallelism configuration.

## Technical Significance
Resolves critical memory overflow issues that prevent Mixtral MoE models from training, improving stability and enabling training on larger models or batch sizes within available NPU memory constraints.

## Related
- `technique-moe` / `technique-memory-optimization` / `technique-gradient-checkpointing`