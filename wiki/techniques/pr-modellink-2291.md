---
id: technique-pr-modellink-2291
title: "PR Insight: Ascend/ModelLink #2291"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - attention
  - layernorm
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2291"
---

# PR Insight: Ascend/ModelLink #2291

**Title:** move final norms out of decoder for MTP

## Overview
Optimizes the MTP (Multi-Task Prediction) architecture by moving final layer normalization operations outside of the decoder block. This reorganization improves computational efficiency and memory usage.

## Technical Significance
Performance optimization that reduces redundant computation and improves kernel fusion opportunities. Moving layernorm operations can enable better operator fusion and reduce memory bandwidth requirements during inference and training.

## Related
- technique-layernorm
- technique-operator-fusion