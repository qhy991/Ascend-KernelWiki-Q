---
id: technique-pr-modellink-2248
title: "PR Insight: Ascend/ModelLink #2248"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - hunyuan
  - data-preprocessing
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2248"
---

# PR Insight: Ascend/ModelLink #2248

**Title:** 【HunyuanLargeMoE】part of data-preprocess

## Overview
Implements data preprocessing components for HunyuanLargeMoE training. This includes data loading, tokenization, and preprocessing pipelines specific to the Hunyuan MoE model requirements.

## Technical Significance
Provides the data infrastructure needed for training HunyuanLargeMoE efficiently on Ascend hardware. Proper data preprocessing is critical for distributed training throughput and memory efficiency, especially for large-scale MoE models.

## Related
- technique-moe
- technique-data-reuse