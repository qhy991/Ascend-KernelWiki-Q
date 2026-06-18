---
id: code-cann-ops-adv-incre-flash-attention
title: "CANN Ops Adv \u2014 Incremental Flash Attention"
type: source-code
repo: Ascend/cann-ops-adv
path: src/transformer/incre_flash_attention
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/incre_flash_attention
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- attention
- flash-attention
- kv-cache
- inference
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- global-memory
- unified-buffer
techniques:
- online-softmax
- kv-cache-paging
- pipeline-scheduling
kernel_types:
- attention
- flash-attention
- paged-attention
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Incremental Flash Attention

Advanced CANN source path for decode/incremental FlashAttention. It anchors evidence for KV-cache reads, small-step decode attention, and mixed Cube/Vector work in autoregressive inference.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/transformer/incre_flash_attention`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/incre_flash_attention
