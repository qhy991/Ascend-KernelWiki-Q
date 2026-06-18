---
id: technique-pr-modellink-2646
title: "PR Insight: Ascend/ModelLink #2646"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - training
  - performance
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2646"
---

# PR Insight: Ascend/ModelLink #2646

**Title:** Performance optimization on get batch

## Overview
This PR optimizes the performance of batch retrieval operations in ModelLink. The get_batch function is critical for efficient data loading during training, and this optimization improves its speed or efficiency on Ascend hardware.

## Technical Significance
Data loading performance is often a bottleneck in training pipelines. Optimizing get_batch reduces data processing overhead, improving overall training throughput on Ascend NPUs and allowing the hardware to spend more time on computation rather than data movement.

## Related
- technique-data-reuse
- technique-unified-buffer