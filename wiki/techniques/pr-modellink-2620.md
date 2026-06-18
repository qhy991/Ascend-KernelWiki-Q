---
id: technique-pr-modellink-2620
title: "PR Insight: Ascend/ModelLink #2620"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen3
  - finetune
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2620"
---

# PR Insight: Ascend/ModelLink #2620

**Title:** add tune qwen3 4b and qwen3 8b

## Overview
This PR adds fine-tuning support for Qwen3 models in 4B and 8B parameter sizes. The implementation extends fine-tuning capabilities to medium-sized models, adding necessary configurations and training scripts.

## Technical Significance
Medium-sized models (4B, 8B) are increasingly popular for production fine-tuning. The implementation must balance compute efficiency with model capacity, using optimized data loading, gradient accumulation, and mixed-precision training on Ascend NPUs.

## Related
- `technique-training-script`