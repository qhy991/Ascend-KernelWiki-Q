---
id: technique-pr-modellink-2744
title: "PR Insight: Ascend/ModelLink #2744"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - performance
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2744"
---

# PR Insight: Ascend/ModelLink #2744

**Title:** 【训练性能】兼容层named_modules递归获取参数性能优化

## Overview
This PR optimizes the performance of recursively retrieving parameters through named_modules in the compatibility layer. The optimization reduces overhead when accessing model parameters during training loops.

## Technical Significance
The named_modules operation is frequently used during training to access model parameters. Optimizing this recursive traversal reduces Python overhead and improves overall training throughput on Ascend NPUs by minimizing parameter access time.

## Related
- technique-operator-fusion