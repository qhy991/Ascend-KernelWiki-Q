---
id: technique-pr-modellink-2580
title: "PR Insight: Ascend/ModelLink #2580"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - embedding
  - performance
  - refactoring
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2580"
---

# PR Insight: Ascend/ModelLink #2580

**Title:** vocab_parallel_embedding_forward 重构引入不亲和操作，导致性能劣化

## Overview
This PR addresses a performance regression caused by refactoring the vocab_parallel_embedding_forward function. The Chinese title indicates that the refactoring introduced non-affine operations, leading to performance degradation.

## Technical Significance
Vocabulary parallel embedding is critical for large language models with large vocabularies. Non-affine operations in embedding forward passes can break data locality and memory access patterns optimized for Ascend NPUs. The fix likely restores efficient memory access, maintains data affinity, or removes operations that break parallelism.

## Related
- `technique-operator-fusion`