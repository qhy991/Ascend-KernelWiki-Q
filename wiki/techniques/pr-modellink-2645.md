---
id: technique-pr-modellink-2645
title: "PR Insight: Ascend/ModelLink #2645"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - mla
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2645"
---

# PR Insight: Ascend/ModelLink #2645

**Title:** [feat]fa support mla with seperate q and k

## Overview
This PR adds support for Multi-Head Latent Attention (MLA) with separate query and key projections in the Flash Attention implementation. MLA is a memory-efficient attention mechanism used in models like DeepSeek that reduces memory footprint by using latent vectors. The change enables the FA kernel to handle split Q and K projection architectures.

## Technical Significance
Enabling MLA with separate Q/K support is critical for training DeepSeek models on Ascend NPU. MLA significantly reduces memory usage in attention layers, which is essential for large-scale training. This feature ensures ModelLink can efficiently train state-of-the-art models using advanced attention optimizations on Ascend hardware.

## Related
- technique-operator-fusion
- technique-attention