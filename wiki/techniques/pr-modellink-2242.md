---
id: technique-pr-modellink-2242
title: "PR Insight: Ascend/ModelLink #2242"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - attention
  - mtp
  - optimization
  - tensor-parallelism
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2242"
---

# PR Insight: Ascend/ModelLink #2242

**Title:** extra token优化, mtp layer重计算和tp支持

## Overview
Implements extra token optimization, adds MTP layer recomputation support, and enables tensor parallelism support. These changes improve memory efficiency and distributed training capabilities.

## Technical Significance
Comprehensive optimization that addresses multiple aspects of training efficiency: extra token processing, memory usage through recomputation, and scalability through tensor parallelism. Together these improvements enable training of larger models on Ascend NPUs.

## Related
- technique-attention
- technique-data-reuse
- technique-hccl-optimization