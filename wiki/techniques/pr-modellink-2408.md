---
id: technique-pr-modellink-2408
title: "PR Insight: Ascend/ModelLink #2408"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - training
  - pipeline-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2408"
---

# PR Insight: Ascend/ModelLink #2408

**Title:** Fix finetune data for PP > 2

## Overview
This PR fixes finetune data handling for pipeline parallelism with more than 2 pipeline stages, ensuring correct data distribution and synchronization across pipeline stages.

## Technical Significance
Pipeline parallelism with >2 stages requires careful data management to avoid correctness issues and performance bottlenecks. This fix ensures that data is properly processed across all pipeline stages.

## Related
- `technique-pipeline-parallel` / `technique-data-distribution` / `technique-fine-tuning`