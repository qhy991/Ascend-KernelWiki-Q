---
id: technique-pr-modellink-2286
title: "PR Insight: Ascend/ModelLink #2286"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - weight-conversion
  - tensor-parallelism
  - deepseek3
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2286"
---

# PR Insight: Ascend/ModelLink #2286

**Title:** deepseek3权重切分支持tp

## Overview
Adds tensor parallelism support for DeepSeek3 weight partitioning. This enables proper weight distribution across multiple devices when using tensor parallelism for DeepSeek3 models.

## Technical Significance
Enables efficient training of DeepSeek3 on multi-NPU setups by supporting tensor parallelism during weight partitioning. Proper weight distribution is essential for maximizing throughput and memory efficiency in distributed training scenarios.

## Related
- technique-moe
- technique-hccl-optimization
- technique-data-reuse