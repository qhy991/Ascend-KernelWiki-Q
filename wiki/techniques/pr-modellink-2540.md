---
id: technique-pr-modellink-2540
title: "PR Insight: Ascend/ModelLink #2540"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - training
  - communication
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2540"
---

# PR Insight: Ascend/ModelLink #2540

**Title:** loss打印all_reduce异步

## Overview
This PR optimizes loss printing by making the all_reduce operation asynchronous. The change decouples loss aggregation from printing, reducing communication overhead and improving training throughput.

## Technical Significance
Loss printing typically requires all-reducing loss values across all ranks for global metrics. Making this asynchronous allows computation to continue while communication happens, hiding latency and improving training efficiency. This is particularly important for distributed training on Ascend NPUs where communication overhead can be significant.

## Related
- `technique-hccl-optimization`