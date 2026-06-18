---
id: technique-pr-mindspeed-2117
title: "PR Insight: Ascend/MindSpeed #2117"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - attention
  - refactor
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2117"
---

# PR Insight: Ascend/MindSpeed #2117

**Title:** refactor：generate mask & ailibi pse

## Overview
This PR refactors the generation of attention masks and ALiBi (Attention with Linear Biases) PSE (Position-Sensitive Encoding) in MindSpeed. The change improves the efficiency of mask generation for various attention types.

## Technical Significance
Efficient mask generation is crucial for attention computation performance on Ascend NPUs. The refactoring optimizes the creation of causal masks, padding masks, and ALiBi position encodings, which are fundamental operations in transformer models. ALiBi provides better extrapolation to longer sequences than traditional position embeddings. The optimization likely reduces memory allocation overhead and improves kernel fusion opportunities for attention operations, particularly beneficial for flash attention implementations on Ascend hardware.

## Related
- `technique-attention`
- `technique-flash-attention`