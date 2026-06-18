---
id: technique-pr-modellink-2418
title: "PR Insight: Ascend/ModelLink #2418"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
  - rotary-embedding
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2418"
---

# PR Insight: Ascend/ModelLink #2418

**Title:** --use-fused-rotary-pos-emb在405B模型上多占用2G显存，改用--use-fused-rotary-pos-emb-new

## Overview
This PR addresses a memory issue where the fused rotary positional embedding operator consumed 2GB extra memory on 405B models, switching to a new implementation with better memory efficiency.

## Technical Significance
Memory optimizations are critical for large models like 405B; switching to a more memory-efficient rotary embedding implementation reduces memory overhead without sacrificing performance, enabling training on hardware with tighter memory constraints.

## Related
- `technique-rotary-embedding` / `technique-memory-optimization` / `technique-operator-fusion`