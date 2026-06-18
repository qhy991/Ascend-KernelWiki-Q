---
id: code-catlass-flash-attention-infer
title: CATLASS Flash Attention Inference Example
type: source-code
repo: Ascend/catlass
path: examples/23_flash_attention_infer
url: https://gitee.com/ascend/catlass/tree/master/examples/23_flash_attention_infer
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- flash-attention
- attention
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- unified-buffer
- global-memory
techniques:
- online-softmax
- kv-cache-paging
- data-reuse
kernel_types:
- attention
- flash-attention
languages:
- cpp
- ascendc
---

# CATLASS Flash Attention Inference Example

CATLASS FlashAttention inference example used as source evidence for streaming attention score/value computation and softmax staging on Ascend.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/23_flash_attention_infer`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/23_flash_attention_infer
