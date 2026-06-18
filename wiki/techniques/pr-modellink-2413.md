---
id: technique-pr-modellink-2413
title: "PR Insight: Ascend/ModelLink #2413"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
  - ulysses
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2413"
---

# PR Insight: Ascend/ModelLink #2413

**Title:** bugfix:ulysses 显存劣化

## Overview
This PR fixes a memory regression issue in Ulysses (a parallelization or optimization technique), which was causing increased memory usage rather than the expected reduction.

## Technical Significance
Memory optimizations should reduce, not increase, memory usage; this fix ensures that Ulysses parallelization provides the intended memory efficiency improvements during training on Ascend hardware.

## Related
- `technique-memory-optimization` / `technique-ulysses` / `technique-parallelization`