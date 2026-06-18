---
id: technique-pr-modellink-2569
title: "PR Insight: Ascend/ModelLink #2569"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - embedding
  - attention
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2569"
---

# PR Insight: Ascend/ModelLink #2569

**Title:** Refact: embedding and rotary embedding

## Overview
This PR refactors the embedding and rotary embedding implementations in ModelLink. The changes improve code structure, maintainability, or performance of these critical model components.

## Technical Significance
Embedding layers and rotary positional embeddings are compute-intensive and memory-bound operations. Refactoring can improve performance through better memory access patterns, fusion opportunities, or more efficient kernel utilization on Ascend NPUs. It also improves code maintainability for future optimizations.

## Related
- `technique-operator-fusion`