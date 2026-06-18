---
id: technique-pr-mindspeed-1171
title: "PR Insight: Ascend/MindSpeed #1171"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - compression
  - determinism
  - algorithm
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1171"
---

# PR Insight: Ascend/MindSpeed #1171

**Title:** 【update】参数副本压缩算法增加确定性计算逻辑分支

## Overview
This PR updates the parameter replica compression algorithm to add a deterministic computation branch. Deterministic computation ensures reproducible results across runs, which is important for debugging and validation.

## Technical Significance
Deterministic compression algorithms are essential for reproducible training on Ascend NPUs. This addition improves the parameter compression feature by ensuring consistent results while maintaining compression benefits, helping users debug and validate models reliably.

## Related
- technique-memory-optimization