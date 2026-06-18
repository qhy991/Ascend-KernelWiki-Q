---
id: technique-pr-modellink-2250
title: "PR Insight: Ascend/ModelLink #2250"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - hunyuan
  - model-architecture
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2250"
---

# PR Insight: Ascend/ModelLink #2250

**Title:** 【HunyuanLargeMoE】part of model

## Overview
Implements part of the model architecture for HunyuanLargeMoE, a large-scale Mixture-of-Experts model. This change adds specific model components and layer definitions to support the Hunyuan MoE architecture in ModelLink.

## Technical Significance
Adds support for a production-grade large MoE model, enabling researchers and engineers to train and deploy HunyuanLargeMoE on Ascend NPUs. This contributes to modellink's coverage of state-of-the-art MoE architectures.

## Related
- technique-moe
- technique-hccl-optimization