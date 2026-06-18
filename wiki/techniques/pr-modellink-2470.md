---
id: technique-pr-modellink-2470
title: "PR Insight: Ascend/ModelLink #2470"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - dskv3
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2470"
---

# PR Insight: Ascend/ModelLink #2470

**Title:** [core-llm][dskv3]mtp loss scaler and fix expert bias dtype

## Overview
This PR addresses MTP loss scaling and fixes expert bias data type issues in the MoE (Mixture of Experts) implementation for DeepSeek V3. Loss scaling is important for mixed-precision training stability.

## Technical Significance
Fixing expert bias dtype ensures correct computation in MoE layers on Ascend hardware. Loss scaling improvements help maintain training stability in mixed-precision FP16/BF16 training for large MoE models.

## Related
- MoE (Mixture of Experts)
- mixed-precision training
- DeepSeek V3