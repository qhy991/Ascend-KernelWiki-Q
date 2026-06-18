---
id: technique-pr-modellink-2609
title: "PR Insight: Ascend/ModelLink #2609"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen3
  - training
  - script
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2609"
---

# PR Insight: Ascend/ModelLink #2609

**Title:** Add Qwen3 4B and Qwen3 8B

## Overview
This PR adds support for Qwen3 models in 4B and 8B parameter sizes. The implementation includes model configurations, training scripts, and possibly weight conversion tools for these medium-sized models.

## Technical Significance
Medium-sized models are popular for production deployment due to their balance of performance and resource requirements. Supporting 4B and 8B Qwen3 models enables efficient training on Ascend NPUs with optimized data loading, mixed-precision training, and distributed training strategies.

## Related
- `technique-training-script`