---
id: technique-pr-modellink-2251
title: "PR Insight: Ascend/ModelLink #2251"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - attention
  - mtp
  - recompute
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2251"
---

# PR Insight: Ascend/ModelLink #2251

**Title:** add recompute mtp layer

## Overview
Adds recompute functionality for MTP (Multi-Task Prediction) layers. This enables activation recomputation to reduce memory usage during training of models with MTP components.

## Technical Significance
Memory optimization that allows training of larger models by recomputing activations instead of storing them. This is particularly useful for MTP layers that may have high memory footprint during backward passes.

## Related
- technique-attention
- technique-data-reuse