---
id: technique-pr-modellink-2740
title: "PR Insight: Ascend/ModelLink #2740"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - performance
  - mindspore
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2740"
---

# PR Insight: Ascend/ModelLink #2740

**Title:** mindspore get_batch performance optimization

## Overview
This PR optimizes the performance of the get_batch operation in the MindSpore backend. The optimization improves data loading efficiency during training by reducing overhead in batch retrieval.

## Technical Significance
Batch loading is a critical component of training performance. Optimizing this operation reduces data pipeline bottlenecks and enables better utilization of Ascend NPUs during training, improving overall training throughput.

## Related
- technique-operator-fusion