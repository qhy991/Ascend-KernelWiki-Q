---
id: technique-pr-modellink-2748
title: "PR Insight: Ascend/ModelLink #2748"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mamba
  - performance
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2748"
---

# PR Insight: Ascend/ModelLink #2748

**Title:** Optimized the performance of mamba2 pretrain.

## Overview
This PR optimizes the performance of Mamba2 model pre-training. It improves training efficiency for state-space models on Ascend NPUs.

## Technical Significance
Mamba2 requires optimized kernels for efficient training. This performance optimization improves throughput and reduces training time for Mamba2 models on Ascend NPUs, making state-space model training more practical.

## Related
- `technique-attention`
- `technique-data-reuse`