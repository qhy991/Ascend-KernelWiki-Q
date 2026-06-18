---
id: technique-pr-modellink-2143
title: "PR Insight: Ascend/ModelLink #2143"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - memory-optimization
  - distributed
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2143"
---

# PR Insight: Ascend/ModelLink #2143

**Title:** 支持moe-zero-memory特性

## Overview
Adds support for the moe-zero-memory feature, which optimizes memory usage for MoE (Mixture-of-Experts) models. This feature reduces memory footprint during MoE training and inference.

## Technical Significance
Memory optimization that enables training of larger MoE models by reducing the memory requirements for expert weights and activations. This is crucial for scaling MoE models on Ascend NPUs with limited device memory.

## Related
- technique-moe
- technique-data-reuse