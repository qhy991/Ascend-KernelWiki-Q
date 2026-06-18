---
id: code-cann-ops-adv-prompt-flash-attention
title: "CANN Ops Adv \u2014 Prompt Flash Attention"
type: source-code
repo: Ascend/cann-ops-adv
path: src/transformer/prompt_flash_attention
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/prompt_flash_attention
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- attention
- flash-attention
- ascendc
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
- pipeline-scheduling
kernel_types:
- attention
- flash-attention
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Prompt Flash Attention

Advanced CANN transformer operator source for prompt-phase FlashAttention. This path is code evidence for attention tiling, score/softmax/value pipeline organization, and inference-oriented memory handling on Ascend.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/transformer/prompt_flash_attention`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/prompt_flash_attention
